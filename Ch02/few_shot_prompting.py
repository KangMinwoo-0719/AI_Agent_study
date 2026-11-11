import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# 로컬에서 .env 파일 환경변수 불러오기
load_dotenv()

# api key 가져오기
my_key = os.getenv("GEMINI_API_KEY")

# client 객체 생성
client = genai.Client(api_key=my_key)

# 퓨샷 프롬프트 작성
few_shot_prompt = """
다음 문장의 감정을 분석하여 '긍정', '부정', '중립' 중 하나로 분류하세요.

문장: "오늘 날씨가 너무 좋아서 기분이 상쾌해."
감정: 긍정

문장: "배송이 일주일이나 늦어져서 정말 짜증난다."
감정: 부정

문장: "내일 오전 10시에 회의가 예정되어 있습니다."
감정: 중립
"""

# 응답 생성하기
response = client.models.generate_content(
 
    # 모델 지정
    model="gemini-3.5-flash-lite",

    # 퓨삿 프롬프트 구성
    contents=input(),

    config=types.GenerateContentConfig(

        # 답변 창의성 조절
        temperature=0.4,

        # 모델 역할(페르소나) 정의
        system_instruction=few_shot_prompt
    )
)
# 응답 출력
print("---답변---")
print(response.text)