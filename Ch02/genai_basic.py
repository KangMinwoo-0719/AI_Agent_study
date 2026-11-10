import os
from google import genai

# 모델 설정값 타입 모듈 호출
from google.genai import types
from dotenv import load_dotenv

# 로컬 환경 .env 파일 환경변수 읽어오기
load_dotenv()

# .env 파일의 API 키 불러오기
my_key = os.getenv("GEMINI_API_KEY")


# API 통신을 위한 클라이언트 객체 초기화
client = genai.Client(api_key = my_key)

# 모델 호출 및 응답 생성하기
response = client.models.generate_content(

    # 모델 지정
    model="gemini-3.5-flash-lite",

    # 입력 프롬프트 구성
    contents="세상에서 누가 제일 아름답니?",

    config=types.GenerateContentConfig(

        # 답변 창의성 조절(0.0 ~ 1.0)
        temperature=0.3,

        # 모델의 역할(페르소나) 정의
        system_instruction="너는 백설공주 이야기 속의 마법 거울이야. 그 이야기의 캐릭터에" \
        "부합하게 답변해줘."
    )
)

# 생성된 답변 출력
print("---답변---")
print(response.text)