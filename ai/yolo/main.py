# main.py
import io
import uvicorn
import numpy as np
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from ultralytics import YOLO

# =========================
# Config
# =========================
STAGE1_WEIGHTS = "best1.pt"   # 1차: joy/angry/sad/hurt/complex 로 학습한 가중치
STAGE2_WEIGHTS = "best2.pt"   # 2차: embarrassed/anxious 로 학습한 가중치

# ====== 설정 ======
STAGE1_CLASSES = ["joy", "angry", "sad", "hurt", "complex"]
STAGE2_CLASSES = ["embarrassed", "anxious"]
CROP_PAD = 0.06 # CROP_PAD 변수가 정의되지 않아 추가했습니다.

STAGE1_CONF   = 0.25
COMPLEX_GATE  = 0.30        # complex일 때 2차로 보낼 최소 conf
STAGE2_CONF   = 0.25
STAGE2_CONF_FALLBACK = 0.05 # 2차가 안 잡히면 한번 더 완화
DEFAULT_COMPLEX_MAP = "embarrassed"  # 최후 폴백(반드시 six-class 중 하나)

# =========================
# App & CORS
# =========================
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"],
)

# =========================
# Load models (once)
# =========================
stage1 = YOLO(STAGE1_WEIGHTS)   # detect head
stage2 = YOLO(STAGE2_WEIGHTS)   # detect head (2-class)

# =========================
# Helpers
# =========================
def clamp(x, lo, hi): return max(lo, min(hi, x))

def crop_with_pad(img: Image.Image, xyxy, pad_ratio=CROP_PAD) -> Image.Image:
    """xyxy = [x1,y1,x2,y2] 기준으로 6% 패딩을 주어 안전하게 crop"""
    w, h = img.size
    x1, y1, x2, y2 = map(float, xyxy)
    bw, bh = (x2 - x1), (y2 - y1)
    px, py = bw * pad_ratio, bh * pad_ratio
    x1 = clamp(x1 - px, 0, w - 1)
    y1 = clamp(y1 - py, 0, h - 1)
    x2 = clamp(x2 + px, 0, w - 1)
    y2 = clamp(y2 + py, 0, h - 1)
    return img.crop((x1, y1, x2, y2))

def parse_top_box(results):
    """
    Ultralytics 결과에서 가장 높은 conf 한 개만 추출
    return (class_id, conf, xyxy) or (None, None, None)
    """
    for r in results:
        if r.boxes is None or len(r.boxes) == 0:
            continue
        # 이미 NMS가 적용되어 conf 내림차순 정렬 상태
        b = r.boxes[0]
        cls_id = int(b.cls)
        conf = float(b.conf)
        xyxy = [float(v) for v in b.xyxy[0]]
        return cls_id, conf, xyxy
    return None, None, None

# =========================
# API
# =========================
@app.post("/predict_emotion")
async def predict_emotion(file: UploadFile = File(...)):
    # 1) 이미지 로드
    raw = await file.read()
    try:
        img = Image.open(io.BytesIO(raw)).convert("RGB")
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid image file")

    # 2) 1차 추론 (joy/angry/sad/hurt/complex)
    r1 = stage1(img, conf=STAGE1_CONF)
    cls1, conf1, box1 = parse_top_box(r1)

    if cls1 is None:
        # 아무 것도 못 찾았으면 neutral로 정규화
        return {"stage": "stage1", "emotion": "neutral", "confidence": 0.0, "bounding_box": []}

    pred1 = STAGE1_CLASSES[cls1]

    # 3) complex면 2차 추론으로 (최종 출력은 항상 6클래스)
    if pred1 == "complex" and conf1 >= COMPLEX_GATE:
        face_crop = crop_with_pad(img, box1, pad_ratio=CROP_PAD)

        # 2차 1st pass
        r2 = stage2(face_crop, conf=STAGE2_CONF)
        cls2, conf2, _ = parse_top_box(r2)

        # 2차가 비었거나 conf 낮으면 2nd pass로 한번 더 완화
        if cls2 is None or conf2 < STAGE2_CONF:
            r2_low = stage2(face_crop, conf=STAGE2_CONF_FALLBACK)
            cls2_low, conf2_low, _ = parse_top_box(r2_low)
            if cls2_low is not None:
                cls2, conf2 = cls2_low, conf2_low

        if cls2 is not None:
            pred2 = STAGE2_CLASSES[cls2]
            return {
                "stage": "stage2",
                "emotion": pred2,
                "confidence": round(float(conf2), 2),
                "bounding_box": [round(float(x), 2) for x in box1],
                "stage1": {"emotion": pred1, "confidence": round(float(conf1), 2)}
            }

        # ★ 최후 폴백: complex를 지정된 클래스에 강제 매핑
        return {
            "stage": "stage2-fallback",
            "emotion": DEFAULT_COMPLEX_MAP,
            "confidence": round(float(conf1), 2),
            "bounding_box": [round(float(x), 2) for x in box1],
            "stage1": {"emotion": pred1, "confidence": round(float(conf1), 2)}
        }

    # 4) complex가 아니면 1차 결과 그대로
    return {
        "stage": "stage1",
        "emotion": pred1,
        "confidence": round(float(conf1), 2),
        "bounding_box": [round(float(x), 2) for x in box1]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)