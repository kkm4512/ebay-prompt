import openai; import json; import os
from helper.file import *
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("GPT_API_KEY"))

# 📂 instruction 폴더 안의 messageValidatePrompt.md 파일을 불러오기
PROMPT_PATH = os.path.join("instruction", "messageValidatePrompt.md")
PROMPT_TEMPLATE = loadPromptFromMarkdown(PROMPT_PATH)

def validate_response_with_ai(ai_response):
    print("AI 응답 검증 시작 ... ✅ ")

    # 📌 프롬프트에서 동적으로 데이터를 삽입
    prompt = PROMPT_TEMPLATE.replace("{request}", ai_response["request"]) \
                         .replace("{category}", ai_response["category"]) \
                         .replace("{response}", ai_response["response"])
    

    response = client.chat.completions.create(
        model=os.getenv("GPT_MODEL"),
        messages=[
            {"role": "system", "content": "당신은 AI 응답을 검증하는 시스템입니다. 응답이 적절한지 분석하세요."},
            {"role": "user", "content": prompt}
        ]
    )
    try:
        response_json = json.loads(response.choices[0].message.content) 
    except json.JSONDecodeError as e:
        print(" messageCreate로 보낼 데이터 형식: " + response)
        print(f"❌ messageCreate로 보낼 데이터 형식 파싱 오류 발생 !: {e}")
        return
    print("AI 응답 검증 완료 ... 🎉 ")
    return response_json
    
    