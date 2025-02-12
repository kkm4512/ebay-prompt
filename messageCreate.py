import openai
import os
import json
import config.config as config
from messageValidate import validate_response_with_ai
from fileRead import loadPromptFromMarkdown

# OpenAI API 키 설정 (보안을 위해 환경변수 사용 추천)
client = openai.OpenAI(api_key=config.GPT_API_KEY)

# 📂 instruction 폴더 안의 prompt.md 파일을 불러오기
PROMPT_PATH = os.path.join("instruction", "messageCreatePrompt.md")
PROMPT_TEMPLATE = loadPromptFromMarkdown(PROMPT_PATH)

def sendToAi(description):
    # 📌 마크다운에서 불러온 프롬프트를 사용
    prompt = PROMPT_TEMPLATE.replace("{description}", description)

    print("AI 요청 시작 ... ✅")
    response = client.chat.completions.create(
        model=config.GPT_MODEL,
        messages=[
            {"role": "system", "content": "당신은 E-커머스 고객들의 메세지에 응대하는 직원입니다. 사용자의 이메일을 분석하여 적절한 응답을 생성하세요."},
            {"role": "user", "content": prompt}
        ],
        # 창의성 낮추기 (일관성 높임)
        temperature=0
    )
    try:
        response_json = json.loads(response.choices[0].message.content)
    except json.JSONDecodeError as e:
        print("response 형식:" + response)
        print(f"❌messageCreate로 부터 받은 컨텐트 내용 파싱에서 JSON오류 발생 !: {e}")
        return
    verification_response = validate_response_with_ai(response_json)
    verification_response['request'] = response_json['request']
    verification_response['response'] = response_json['response']
    print("AI 응답 완료 ... 🎉")

    return verification_response
