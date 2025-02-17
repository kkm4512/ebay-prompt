# 📌 마크다운 파일을 불러오는 함수
def loadPromptFromMarkdown(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()