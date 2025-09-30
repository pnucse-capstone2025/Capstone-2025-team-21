import os
import torch
import torch.nn as nn
import torch.nn.functional as F
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModel
from typing import Dict, List

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----------------------------
# 1. 모델 아키텍처 정의 (학습 스크립트의 BERTClassifier 클래스와 동일하게)
# ----------------------------
class BERTClassifier(nn.Module):
    # train_ctx_only.py에 정의했던 클래스와 완전히 동일해야 합니다.
    def __init__(self, model_name: str, num_labels: int, dropout: float = 0.2, trainable_layers: int = 12):
        super().__init__()
        self.bert = AutoModel.from_pretrained(model_name)
        hidden_size = self.bert.config.hidden_size
        self.dropout = nn.Dropout(dropout)
        self.classifier = nn.Linear(hidden_size, num_labels)

    def forward(self, input_ids, attention_mask):
        out = self.bert(input_ids=input_ids, attention_mask=attention_mask)
        cls_output = self.dropout(out.last_hidden_state[:,0])
        logits = self.classifier(cls_output)
        return logits

# ----------------------------
# 2. 모델 및 토크나이저 로드 (학습 때와 동일한 정보 사용)
# ----------------------------

# 추론에 사용할 최종 모델 및 토크나이저 정보
MODEL_PATH = 'ctx_best.pt'
TOKENIZER_NAME = 'klue/bert-base'  # <-- (수정 1) 학습 때 사용한 모델명
NUM_LABELS = 6
# label_map.json 파일이나 학습 스크립트를 참고하여 정확하게 맞춰주세요.
ID2LAB_MAP = {0: '상처', 1: '슬픔', 2: '불안', 3: '당황', 4: '분노', 5: '기쁨'}

# GPU 사용 가능 여부 확인
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"사용 장치: {device}")

# 모델 및 토크나이저 로드
try:
    tokenizer = AutoTokenizer.from_pretrained(TOKENIZER_NAME)
    model = BERTClassifier(TOKENIZER_NAME, NUM_LABELS).to(device) # <-- (수정 2) 클래스명 변경
    model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
    model.eval() # 추론 모드로 전환
    print(f"모델 '{MODEL_PATH}' 로드 완료.")
except Exception as e:
    print(f"모델 로드 중 오류 발생: {e}")
    model = None

# ----------------------------
# 3. API 입력 데이터 스키마 정의
# ----------------------------
class EmotionInput(BaseModel):
    prev_user: str
    prev_sys: str
    curr_user: str

# ----------------------------
# 4. 추론 로직을 담은 API 엔드포인트 구현
# ----------------------------
@app.post("/predict_emotion")
async def predict_emotion(input: EmotionInput):
    if model is None:
        return {"error": "모델이 로드되지 않았습니다."}, 500

    # 입력 텍스트를 컨텍스트 형식으로 조합
    if not input.prev_user and not input.prev_sys:
        text = input.curr_user
    else:
        # (수정 3) tokenizer의 sep_token 사용
        sep = tokenizer.sep_token
        text = f"{input.prev_user} {sep} {input.prev_sys} {sep} {input.curr_user}"

    # 모델 입력 데이터 전처리
    encoding = tokenizer(
        text,
        padding='max_length',
        truncation=True,
        max_length=192,
        return_tensors='pt'
    )

    input_ids = encoding['input_ids'].to(device)
    attention_mask = encoding['attention_mask'].to(device)

    # 추론 실행
    with torch.no_grad():
        logits = model(input_ids, attention_mask)

    # 예측 확률 및 라벨 계산
    probabilities = F.softmax(logits, dim=1).squeeze(0)
    predicted_id = torch.argmax(probabilities).item()
    predicted_label = ID2LAB_MAP.get(predicted_id, "알 수 없음") # .get()으로 안전하게 접근
    confidence = probabilities[predicted_id].item()

    # 결과 반환
    return {
        "predicted_label": predicted_label,
        "confidence": confidence,
        "all_probabilities": {
            ID2LAB_MAP.get(i, f"unknown_{i}"): prob.item() for i, prob in enumerate(probabilities)
        }
    }