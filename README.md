# 치매노노: AI 기반 추억 앨범 및 치매 예방 서비스

## 1. 프로젝트 배경

### 1.1. 국내외 시장 현황 및 문제점

대한민국은 초고령 사회에 진입했으며, 이로 인해 치매 유병률과 관리 비용이 급증하는 사회적 문제에 직면했다. 기존의 치매 예방 및 정서 지원을 위한 회상 요법은 대부분 전문가와의 대면으로 이루어져 시간, 장소, 비용 측면에서 제약이 컸다. 이를 보완하기 위해 디지털 프로그램들이 등장했지만, 대부분 정적 콘텐츠 제공에 그쳐 사용자와의 깊은 정서적 교감이나 개인화된 상호작용을 제공하는 데 한계가 있었다. 특히, 고령층의 미묘한 감정을 단일 방식(텍스트 또는 표정)만으로 정확히 파악하기 어렵고, 텍스트 입력 중심의 인터페이스는 디지털 접근성을 저해하는 요인이었다.

### 1.2. 필요성과 기대효과

이러한 문제점을 해결하기 위해, 임상적으로 효과가 검증된 회상 요법을 AI 기술과 결합한 디지털 솔루션이 필요했다. 본 프로젝트는 시공간 제약 없이 접근 가능한 대화형 AI를 통해 확장 가능하고 비용 효율적인 치매 예방 및 정서 지원 서비스를 제공하고자 했다.

**기대효과**는 다음과 같다.

- **인지 기능 강화:** AI와의 대화를 통해 시니어의 장기 기억을 자극하고 인지 능력 유지를 돕는다.
- **정서적 안정 및 고립감 해소:** 멀티모달 감정 인식을 통해 사용자의 감정에 공감하고 적응적인 피드백을 제공하여 정서적 유대감을 형성한다.
- **세대 간 소통 증진:** 대화 내용을 바탕으로 생성된 '추억 앨범'을 가족과 공유하며 자연스러운 소통의 매개체 역할을 하고, 세대 간 유대감을 강화한다.

## 2. 개발 목표

### 2.1. 목표 및 세부 내용

멀티모달 대화형 AI를 기반으로 한 디지털 회상 요법 플랫폼을 구축하여, 시니어의 정신 건강 증진과 가족 간의 유대 강화를 돕는 것을 최종 목표로 했다.

**주요 기능 및 기획 내용:**

1. **AI 기반 회상 요법 대화:** 사용자의 표정과 음성을 실시간으로 분석하여 감정을 파악하고, 이를 바탕으로 개인화된 회상 대화를 진행한다.
2. **자동 추억 앨범(일기) 생성:** AI와의 대화 내용과 감정 흐름을 분석하여 한 편의 일기로 자동 생성하고, 내용에 어울리는 음악과 앨범 표지를 추천한다.
3. **가족과의 소통 기능:** 생성된 앨범을 가족에게 공유할 수 있으며, 가족은 사진을 추가하거나 댓글을 작성하며 시니어의 추억에 함께 참여할 수 있다.
4. **고령자 친화적 UI/UX:** 카카오 소셜 로그인, 음성 중심의 인터페이스, 최소한의 터치로 조작 가능한 화면을 제공하여 디지털 기기 사용이 어려운 시니어의 접근성을 높였다.

### 2.2. 기존 서비스 대비 차별성

본 서비스는 단순히 기술을 개별적으로 적용한 것이 아닌, **임상적 치료법(회상 요법), 멀티모달 AI, 소셜 네트워킹 기능을 유기적으로 통합**했다는 점에서 차별성을 가진다.

- **깊이 있는 정서적 교감:** 표정(YOLOv8)과 발화 내용(KLUE-BERT)을 함께 분석하는 멀티모달 감정 인식을 통해 사용자의 복합적인 감정 상태를 더 정확하게 이해하고 공감 기반의 상호작용을 제공한다.
- **치료적 대화 설계:** 회상 요법 가이드라인에 따라 체계적으로 설계된 질문 데이터베이스를 활용하여, 단순한 일상 대화를 넘어 치료적 효과를 극대화했다.
- **사회적 연결 촉진:** 대화의 결과물을 '앨범'이라는 매개체로 구조화하여, 단순한 기록을 넘어 가족과의 실질적인 소통과 관계 증진으로 이어지도록 설계했다.

### 2.3. 사회적 가치 도입 계획

- **공공성:** 급증하는 치매 관리 비용과 노년층의 정서적 고립이라는 사회적 문제 해결에 기여한다. 디지털 플랫폼을 통해 저비용으로 양질의 서비스를 제공하여 돌봄 격차를 해소하는 데 이바지한다.
- **지속 가능성:** 일회성 이벤트가 아닌, 일상에서 지속적으로 사용할 수 있는 서비스를 제공함으로써 시니어의 장기적인 정신 건강 관리를 지원하고, 가족 관계의 긍정적인 변화를 유도한다.

## 3. 시스템 설계

### 3.1. 시스템 구성도

![Image](https://github.com/user-attachments/assets/acc0457e-6c0e-4550-8f1c-c4c40c0b44af)

### 3.2. 사용 기술

- **프론트엔드:** `React Native`, `Expo`, `TypeScript`, `Context API`
- **백엔드:** `Spring Boot`, `JPA`, `MySQL`
- **AI:**
  - **Model Serving:** `FastAPI`
  - **Frameworks:** `LangChain`
  - **Models:** `YOLOv8` (표정 분석), `KLUE-BERT` (텍스트 분석), `GPT-4o mini` (생성)
- **인프라:** `Docker`, `AWS (S3, RDS)`, `Google Cloud Platform (Cloud Run, VM)`

## 4. 개발 결과

### 4.1. 전체 시스템 흐름도

1. **대화 시작:** 사용자가 메인 화면에서 질문을 선택하면 AI와의 대화 세션이 시작된다.
2. **사용자 발화 및 인식:** 사용자가 마이크에 대고 답변하면, 음성은 STT(Speech-to-Text)로 변환되고, 동시에 카메라는 사용자의 표정을 주기적으로 캡처한다.
3. **멀티모달 감정 분석:** 변환된 텍스트와 캡처된 표정 이미지는 각각 KLUE-BERT와 YOLOv8 모델로 전송되어 감정 확률 분포를 얻는다. 두 결과는 가중 합산(Late Fusion)을 통해 하나의 통합된 감정으로 결론 내려진다.
4. **AI 응답 생성:** 분석된 감정과 대화 맥락을 기반으로 GPT 모델이 회상 요법에 맞는 다음 질문이나 공감 표현을 생성하고, 이는 TTS(Text-to-Speech)를 통해 음성으로 사용자에게 전달된다.
5. **대화 종료 및 후처리:** 대화가 종료되면, 전체 대화 내용과 감정 흐름 분석 결과가 백그라운드에서 비동기적으로 처리된다.
6. **앨범 생성 및 공유:** GPT 모델이 대화를 요약하고 감정 흐름을 반영하여 최종 일기를 생성한다. 이 일기는 음악, 표지와 함께 앨범 형태로 저장되며 사용자는 이를 가족과 공유할 수 있다.

### 4.2. 기능 설명 및 주요 기능 명세서

- **멀티모달 감정 분석:**
  - **입력:** 사용자의 음성 녹음 파일, 실시간 카메라 프레임 이미지
  - **처리:** 음성을 텍스트로 변환 후 KLUE-BERT로 6가지 감정(기쁨, 슬픔, 분노 등) 분석. 카메라 프레임에서 YOLOv8로 얼굴을 탐지하고 6가지 감정으로 분류. 두 분석 결과를 신뢰도에 따라 가중 결합하여 최종 감정 도출.
  - **출력:** 발화 단위의 최종 감정 라벨(e.g., '기쁨') 및 신뢰도 점수.
- **AI 기반 앨범(일기) 자동 생성:**
  - **입력:** 한 세션의 전체 대화 텍스트, 턴별 감정 분석 결과 시퀀스.
  - **처리:** LangChain 파이프라인을 통해 (1)대화 내용 요약, (2)감정 흐름을 반영한 `DiaryPlan` 생성, (3)DiaryPlan을 바탕으로 최종 일기 텍스트 생성, (4)일기 톤에 맞는 음악 추천.
  - **출력:** 서사 구조를 갖춘 일기 텍스트, 추천 음악 정보(제목, 아티스트, YouTube 링크), 추천 앨범 표지.
- **가족 연동 및 소셜 기능:**
  - **입력:** 보호자의 시니어 전화번호 입력, 시니어의 연결 수락, 보호자의 사진/댓글 업로드.
  - **처리:** 다대다(N:M) 관계로 시니어와 가족 계정 연결. 공유된 앨범에 대한 CRUD(생성, 읽기, 수정, 삭제) 기능 수행.
  - **출력:** 연결된 가족에게 공유 앨범 표시, 앨범 내 사진 및 댓글 목록 표시.

### 4.3. 디렉토리 구조

```
Capstone-2025-team-21/
├── ai/                                    # AI 서비스
│   ├── klue-bert/                         # KLUE-BERT 기반 텍스트 감정 분석
│   │   ├── main.py                        # FastAPI 서버
│   │   ├── requirements.txt               # Python 의존성
│   │   └── ctx_best.pt                    # 모델 파일 (다운로드 필요)
│   │
│   └── yolo/                              # YOLO 기반 얼굴 감정 인식
│       ├── main.py                        # FastAPI 서버
│       ├── requirements.txt               # Python 의존성
│       ├── best1.pt                       # 모델 파일 (다운로드 필요)
│       └── best2.pt                       # 모델 파일 (다운로드 필요)
│
├── frontend_mobile/                       # React Native 프론트엔드
│   ├── App.tsx                            # 앱 진입점
│   ├── components/                        # 재사용 가능한 UI 컴포넌트
│   │   ├── AICharacter.tsx                # AI 캐릭터 컴포넌트
│   │   ├── AlbumCard.tsx                  # 앨범 카드
│   │   ├── AlbumHero.tsx                  # 앨범 히어로 섹션
│   │   ├── AlbumView.tsx                  # 앨범 뷰어
│   │   ├── ChatBallon.tsx                 # 채팅 말풍선
│   │   ├── ConversationFlow.tsx           # 대화 플로우
│   │   ├── AnswerMic.tsx                  # 음성 답변 버튼
│   │   └── ...                            # 기타 UI 컴포넌트들
│   │
│   ├── screens/                           # 화면 컴포넌트
│   │   ├── Home.tsx                       # 메인 홈 화면
│   │   ├── Chat.tsx                       # 채팅 화면
│   │   ├── Conversation.tsx               # 대화 화면
│   │   ├── Album.tsx                      # 앨범 목록
│   │   ├── AlbumDetail.tsx                # 앨범 상세
│   │   ├── Login.tsx                      # 로그인 화면
│   │   ├── GuardianMain.tsx               # 보호자 메인
│   │   ├── DiaryResult.tsx                # 일기 결과
│   │   └── ...                            # 기타 화면들
│   │
│   ├── services/                          # 비즈니스 로직 서비스
│   │   ├── api/                           # API 통신
│   │   ├── audio/                         # 오디오 처리
│   │   ├── cameraService.ts               # 카메라 서비스
│   │   ├── conversationService.ts         # 대화 관리
│   │   ├── diaryService.ts                # 일기 기능
│   │   ├── emotionService.ts              # 감정 분석
│   │   ├── faceDetectionService.ts        # 얼굴 감지
│   │   ├── faceRecognitionService.ts      # 얼굴 인식
│   │   ├── kakaoAuthService.ts            # 카카오 인증
│   │   ├── guardianService.ts             # 보호자 기능
│   │   └── ...                            # 기타 서비스들
│   │
│   ├── contexts/                          # React Context 상태 관리
│   │   ├── UserContext.tsx                # 사용자 상태
│   │   ├── ConversationContext.tsx        # 대화 상태
│   │   └── DiaryContext.tsx               # 일기 상태
│   │
│   ├── hooks/                             # 커스텀 훅
│   │   ├── useConversation.ts             # 대화 관련 훅
│   │   ├── useCameraTest.ts               # 카메라 테스트
│   │   ├── useMicrophoneTest.ts           # 마이크 테스트
│   │   └── ...                            # 기타 커스텀 훅들
│   │
│   ├── types/                             # TypeScript 타입 정의
│   ├── utils/                             # 유틸리티 함수
│   │   ├── cameraUtils.ts                 # 카메라 유틸리티
│   │   ├── conversationUtils.ts           # 대화 유틸리티
│   │   ├── microphoneTestUtils.ts         # 마이크 테스트
│   │   └── userUtils.ts                   # 사용자 유틸리티
│   │
│   ├── styles/                            # 스타일 관련 파일
│   ├── assets/                            # 이미지, 폰트 등 정적 자원
│   ├── mocks/                             # 테스트용 목 데이터
│   ├── config/                            # 설정 파일들
│   └── constants/                         # 상수 정의
│
├── backend/                               # Spring Boot 백엔드
│   └── src/main/java/com/chimaenono/dearmind/
│       ├── DearmindApplication.java       # Spring Boot 메인 클래스
│       │
│       ├── album/                         # 앨범 관리
│       │   ├── AlbumController.java
│       │   ├── AlbumPhoto.java
│       │   └── AlbumComment.java
│       │
│       ├── camera/                        # 카메라 기능
│       │   ├── CameraController.java
│       │   └── CameraService.java
│       │
│       ├── config/                        # 설정 클래스
│       │   ├── SecurityConfig.java
│       │   ├── JwtConfig.java
│       │   ├── WebSocketConfig.java
│       │   └── SwaggerConfig.java
│       │
│       ├── conversation/                  # 대화 관리
│       │   ├── ConversationController.java
│       │   ├── ConversationService.java
│       │   └── EmotionFlowService.java
│       │
│       ├── ConversationMessage/           # 대화 메시지
│       │   ├── ConversationMessageController.java
│       │   └── ConversationMessageService.java
│       │
│       ├── diary/                         # 일기 기능
│       │   ├── DiaryPlan.java
│       │   └── EmotionFlow.java
│       │
│       ├── gpt/                           # GPT AI 서비스
│       │   ├── GPTController.java
│       │   └── GPTService.java
│       │
│       ├── guardian/                      # 보호자 기능
│       │   └── GuardianSeniorRelationship.java
│       │
│       ├── microphone/                    # 마이크 기능
│       │   ├── MicrophoneController.java
│       │   └── MicrophoneService.java
│       │
│       ├── music/                         # 음악 추천
│       │   ├── MusicRecommendation.java
│       │   └── YouTubeSearchService.java
│       │
│       ├── notification/                  # 알림 기능
│       │   ├── NotificationController.java
│       │   └── NotificationWebSocketHandler.java
│       │
│       ├── question/                      # 질문 관리
│       │   └── QuestionController.java
│       │
│       ├── s3/                            # AWS S3 파일 업로드
│       │   ├── S3Controller.java
│       │   └── S3Service.java
│       │
│       ├── stt/                           # Speech-to-Text
│       │   ├── STTController.java
│       │   └── STTService.java
│       │
│       ├── tts/                           # Text-to-Speech
│       │   ├── TTSController.java
│       │   └── TTSService.java
│       │
│       ├── user/                          # 사용자 관리
│       │   ├── UserController.java
│       │   ├── KakaoAuthController.java
│       │   └── User.java
│       │
│       └── userEmotionAnalysis/           # 감정 분석
│           ├── UserEmotionAnalysisController.java
│           └── CombineEmotionService.java
│
├── docs/                                  # 문서
│   ├── 01.보고서/                         # 보고서
│   ├── 02.포스터/                         # 포스터
│   └── 03.발표자료/                       # 발표자료
│
├── install_and_build.sh                  # 설치 스크립트
├── README.md                              # 프로젝트 설명서
└── SAMPLE_README.md                       # README 샘플
```

### 4.4. 모델 파일 다운로드

GitHub 파일 크기 제한으로 인해 학습된 모델 파일들은 별도로 다운로드해야 합니다.

**다운로드 링크:**
- [Google Drive - AI 모델 파일](https://drive.google.com/drive/folders/YOUR_FOLDER_ID)

**다운로드 후 설치 방법:**

1. **KLUE-BERT 모델**
   ```bash
   # Google Drive에서 다운로드한 ctx_best.pt 파일을 다음 경로에 저장
   # ctx_best.pt 파일을 ai/klue-bert/ 디렉토리에 복사
   ```

2. **YOLO 모델**
   ```bash
   # Google Drive에서 다운로드한 모델 파일들을 다음 경로에 저장
   # best1.pt, best2.pt 파일들을 ai/yolo/ 디렉토리에 복사
   ```

**모델 파일 목록:**
- `ctx_best.pt` (422MB) - KLUE-BERT 텍스트 감정 분석 모델
- `best1.pt` - YOLO 1차 모델 (joy/angry/sad/hurt/complex 감정)
- `best2.pt` - YOLO 2차 모델 (embarrassed/anxious 감정)

## 5. 설치 및 실행 방법

### 배포 사이트 : https://seniordigitalalbum.github.io

### 5.1. 설치절차 및 실행 방법

#### 사전 요구사항

**공통 요구사항**
- **Node.js** 18.x 이상
- **Python** 3.9 이상
- **Java** 17 이상
- **MySQL** 8.0 이상
- **Docker** (선택사항)

**추가 요구사항**
- **AWS S3** 계정 (파일 저장용)
- **카카오 개발자 계정** (소셜 로그인용)
- **OpenAI API 키** (GPT 서비스용)
- **Google Cloud 계정** (STT/TTS 서비스용)

#### 로컬 설치 및 실행 방법

**1. 저장소 클론**

```bash
git clone <repository-url>
cd Capstone-2025-team-21
```

**2. 데이터베이스 설정**

```bash
# MySQL 데이터베이스 생성
mysql -u root -p
CREATE DATABASE dearmind;
```

**3. Backend 설정 및 실행**

```bash
cd backend

# Gradle 빌드
./gradlew build

# 환경 변수 설정 (application-local.yml 수정)
# - MySQL 연결 정보
# - AWS S3 설정
# - 카카오 REST API 키
## 이 때 모바일 환경 로그인을 위하여 redirect_url을 http://<현재 LAN의 IP 주소>:8080/api/auth/kakao/callback로 설정해주어야 합니다.
## 카카오 개발자 콘솔에서도 해당 redirect_url을 등록합니다.
# - OpenAI API 키
# - Google Cloud 인증서

# 애플리케이션 실행
./gradlew bootRun
```

**Backend 서버**: `http://localhost:8080`

**4. AI 서비스 설정 및 실행**

**KLUE-BERT 서비스 (텍스트 감정 인식)**

```bash
cd ai/klue-bert

# 모델 파일 다운로드 (Google Drive에서)
# ctx_best.pt 파일을 ai/klue-bert/ 디렉토리에 저장

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 서비스 실행
python main.py
```

**KLUE-BERT 서비스**: `http://localhost:8000`

**YOLO 서비스 (얼굴 감정 인식)**

```bash
cd ai/yolo

# 모델 파일 다운로드 (Google Drive에서)
# best1.pt, best2.pt 파일들을 ai/yolo/ 디렉토리에 저장

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt

# 서비스 실행
python main.py
```

**YOLO 서비스**: `http://localhost:8001`

**5. Frontend 설정 및 실행**

```bash
cd frontend_mobile

# 의존성 설치
npm install

# 웹 개발 서버 실행
npx expo start --web

# 모바일 EXPO GO 실행
npx expo start
```

**Frontend 앱**: `http://localhost:8081`
**Frontend 웹**: `http://localhost:8082`

#### Docker를 이용한 실행 (선택사항)

**Backend Docker 실행**

```bash
cd backend
docker build -t dearmind-backend .
docker run -p 8080:8080 dearmind-backend
```

**YOLO 서비스 Docker 실행**

```bash
cd ai/yolo
docker build -t dearmind-yolo .
docker run -p 8001:8001 dearmind-yolo
```

#### 환경 설정

**Backend 환경 변수 (application-local.yml)**

```yaml
spring:
  datasource:
    url: jdbc:mysql://localhost:3306/dearmind
    username: your_username
    password: your_password

aws:
  s3:
    bucket-name: your-bucket-name
    access-key: your-access-key
    secret-key: your-secret-key

kakao:
  client-id: your-kakao-client-id
  client-secret: your-kakao-client-secret

openai:
  api-key: your-openai-api-key

google:
  credentials-path: path/to/google-cloud-credentials.json
```

**Frontend 환경 설정**

```bash
# .env 파일 생성
cd frontend
echo "API_BASE_URL=http://localhost:8080" > .env
echo "KLUE_BERT_API_URL=http://localhost:8000" >> .env
echo "YOLO_API_URL=http://localhost:8001" >> .env
```

**서비스 상태 확인**

```bash
# Backend 상태 확인
curl http://localhost:8080/health

# KLUE-BERT 상태 확인
curl http://localhost:8000/health

# YOLO 상태 확인
curl http://localhost:8001/health
```

### 5.2. 오류 발생 시 해결 방법

#### 일반적인 문제
- **포트 충돌**: `netstat -ano | findstr :8080`으로 확인 후 `taskkill /PID <PID> /F`로 종료
- **의존성 오류**: Node.js 18+, Python 3.9+, Java 17+ 버전 확인 후 `npm ci`, `./gradlew clean build`, `pip install -r requirements.txt` 재실행
- **데이터베이스 연결**: MySQL 서비스 실행 확인 (`net start mysql80` 또는 `brew services start mysql`)

#### AI 서비스 관련 문제
- **모델 파일 없음**: Google Drive에서 모델 파일을 다운로드하여 `ai/klue-bert/`, `ai/yolo/` 디렉토리에 저장
- **메모리 부족**: `export CUDA_VISIBLE_DEVICES=""`로 CPU 모드 실행
- **모델 로딩 실패**: 모델 파일 경로와 권한 확인

#### 기타 오류
- **Backend**: `application-local.yml`에서 데이터베이스, S3, 카카오 API 설정 확인
- **Frontend**: `.env` 파일의 API URL 설정 확인, `npx expo start --clear`로 캐시 클리어

## 6. 소개 자료 및 시연 영상

### 6.1. 프로젝트 소개 자료**Frontend 앱**: `http://localhost:8081`

- [프로젝트 발표 PPT 링크]()

### 6.2. 시연 영상

- [서비스 시연 영상 YouTube 링크](https://youtu.be/bHZ7OJzTG7E?si=DetfMMsPr-eKhrxs)

## 7. 팀 구성

### 7.1. 팀원별 소개 및 역할 분담

| 학번 | 성명 | 역할 |
| :--- | :--- | :--- |
| 202155514 | 김나림 | 아이디어 기획, KLUE-BERT 기반 텍스트 감정 분석 모델 구축, 프론트엔드 개발 및 배포, 로그인 및 시니어-가족 연결 기능 개발 |
| 202155540 | 김채현 | YOLO 기반 표정 감정 분석 모델 구축 및 배포, 감정 통합 및 감정 흐름 로직 구현, LLM 구축, 백엔드 개발 및 배포, DB 구축 및 배포 |

### 7.2. 팀원 별 참여 후기

- **김나림:** ()
- **김채현:** ()

## 8. 참고 문헌 및 출처

1. N. Majumder, S. Poria, D. Hazarika, R. Mihalcea, A. Gelbukh, and E. Cambria, "DialogueRNN: An Attentive RNN for Emotion Detection in Conversations," Proc. of the AAAI Conference on Artificial Intelligence, Vol. 33, pp. 6818-6825, 2019.
2. W. Jiao, H. Yang, I. King, and M. R. Lyu, "HiGRU: Hierarchical Gated Recurrent Units for Utterance-level Emotion Recognition," Proc. of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies (NAACL-HLT 2019), pp. 397-406, 2019.
3. J. Devlin, M. Chang, K. Lee, and K. Toutanova, "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding," NAACL-HLT 2019, pp. 4171-4186, 2019.
5. R. Ekman and W. V. Friesen, "Facial Action Coding System: A Technique for the Measurement of Facial Movement," Consulting Psychologists Press, 1978.