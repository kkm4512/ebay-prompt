import pandas as pd
import random  # 랜덤 숫자 생성을 위한 모듈

def getRandomDataFromEbayExcel():
    # 엑셀 파일 경로 (로컬 파일)
    file_path = "/Users/t2023-m0072/Desktop/ebay/ebay-messages.xlsx"

    # 엑셀 파일 읽기
    df = pd.read_excel(file_path)

    # 랜덤한 행 번호 선택 (1~7407, pandas는 0부터 시작하므로 0~7406)
    random_index = random.randint(0, 7406)  

    # E열(5번째 열)의 해당 행 데이터 가져오기
    return df.iloc[random_index, 4]

def getRandomDatasFromEbayExcel(i):
    # 📌 엑셀 파일 경로
    file_path = "/Users/t2023-m0072/Desktop/ebay/ebay-messages.xlsx"

    # 📌 엑셀 파일 읽기 (첫 번째 행을 컬럼명으로 설정)
    df = pd.read_excel(file_path, header=0)

    # 📌 실제 행 개수를 기반으로 i 값을 조정
    max_rows = df.shape[0]  # 전체 행 개수

    if max_rows < 1:
        raise ValueError("랜덤 샘플을 생성할 충분한 데이터가 없습니다.")

    # 📌 랜덤한 행 선택 (0 ~ max_rows - 1 사이에서 선택)
    random_index = random.randint(0, max_rows - 1)

    # 📌 가져올 범위 설정 (random_index ~ random_index + i)
    end_index = min(random_index + i, max_rows)  # 데이터 범위를 벗어나지 않도록 조정

    # 📌 E열(5번째 열)의 해당 행 데이터 가져오기 (NaN 제거 & 리스트 변환)
    result = df.iloc[random_index:end_index, 4].dropna().tolist()  # 리스트 변환 후 반환

    return result

def get_GENERAL_FromEbayCategoryExcel():
    file_path = "/Users/t2023-m0072/Desktop/ebay/ebay-category.xlsx"
    df = pd.read_excel(file_path, header=0)
    return df.iloc[1:11, 4].dropna().tolist()  

def get_PRICE_NEGOTIATION_FromEbayCategoryExcel():
    file_path = "/Users/t2023-m0072/Desktop/ebay/ebay-category.xlsx"
    df = pd.read_excel(file_path, header=0)
    return df.iloc[11:21, 4].dropna().tolist()

def get_REFUND_FromEbayCategoryExcel():
    file_path = "/Users/t2023-m0072/Desktop/ebay/ebay-category.xlsx"
    df = pd.read_excel(file_path, header=0)
    return df.iloc[21:31, 4].dropna().tolist()

def get_API_REQUIRED_FromEbayCategoryExcel():
    file_path = "/Users/t2023-m0072/Desktop/ebay/ebay-category.xlsx"
    df = pd.read_excel(file_path, header=0)
    return df.iloc[31:41, 4].dropna().tolist()

def get_HUMAN_REVIEW_FromEbayCategoryExcel():
    file_path = "/Users/t2023-m0072/Desktop/ebay/ebay-category.xlsx"
    df = pd.read_excel(file_path, header=0)
    return df.iloc[41:51, 4].dropna().tolist() 

