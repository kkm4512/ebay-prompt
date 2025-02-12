from messageCreate import sendToAi
import json
from excel import getRandomDataFromEbayExcel, getRandomDatasFromEbayExcel, get_GENERAL_FromEbayCategoryExcel, get_PRICE_NEGOTIATION_FromEbayCategoryExcel, get_REFUND_FromEbayCategoryExcel, get_API_REQUIRED_FromEbayCategoryExcel, get_HUMAN_REVIEW_FromEbayCategoryExcel

# Helper Method
def invalidData(data, response, verifyCategory):
    AI_Select_Category = response['category']
    response_stirng = json.dumps(response,ensure_ascii=False)
    if (verifyCategory == AI_Select_Category):
        print("카테고리 일치 ✅")
        print("검증 성공 요청 텍스트: " + data)
        print("검증 성공 응답 텍스트: " + response['response'])
        print("")
        return True
    else:
        print("카테고리 불일치 ❌")
        print("검증 실패 요청 텍스트: " + data)
        print("검증 카테고리: " + verifyCategory)
        print("AI 카테고리: " + AI_Select_Category)
        print("검증 실패 데이터: " + response_stirng)
        print("")
        return False

# ebay 데이터 하나만 테스트
def getRandomDataFromEbayExcelFunction():
    data = getRandomDataFromEbayExcel()
    print("사용자 요청 텍스트: " + data)
    sendToAi(data) 


# ebay 데이터 무작위로 여러개 테스트
def getRandomDatasFromEbayExcelFunction():
    datas = getRandomDatasFromEbayExcel(3) 
    for data in datas: 
        print("사용자 요청 텍스트: " + data)
        sendToAi(data)  
        print("") 

# ebay-category / TYPE / 테스트 - (직접 넣은 데이터 한개, 한번씩만 검증)        
def check_TYPE_FromEbayCategoryExcelFunction(type, data):
    response = sendToAi(data)  
    invalidData(data,response,type)

# ebay-category / GENERAL / 테스트 - (데이터 여러개, 한번씩만 검증)
def get_GENERAL_FromEbayCategoryExcelFunction():
    datas = get_GENERAL_FromEbayCategoryExcel() 
    for data in datas: 
        response = sendToAi(data)  
        invalidData(data,response,"GENERAL")

# ebay-category / GENERAL / 테스트 - (데이터 여러개, 여러개 검증)
def get_GENERAL_FromEbayCategoryExcelFunction_Many():
    datas = get_GENERAL_FromEbayCategoryExcel() 
    count = 0
    for data in datas: 
        for i in range(0,10):
            response = sendToAi(data)  
            invalidResponse = invalidData(data,response,"GENERAL")
            if (invalidResponse):
                count+=1
    if (count == 10):
        print("10번의 결과가 모두 일치합니다! ✅") 
    else:
        print("10번의 결과중, " + count + "번이 틀렸습니다! ❌") 

# ebay-category / PRICE_NEGOTIATION / 테스트 - (데이터 여러개, 한번씩만 검증)
def get_PRICE_NEGOTIATION_FromEbayCategoryExcelFunction():
    datas = get_PRICE_NEGOTIATION_FromEbayCategoryExcel() 
    for data in datas: 
        response = sendToAi(data)  
        invalidData(data,response,"PRICE_NEGOTIATION")

# ebay-category / REFUND / 테스트 - (데이터 여러개, 한번씩만 검증)
def get_REFUND_FromEbayCategoryExcelFunction():
    datas = get_REFUND_FromEbayCategoryExcel() 
    for data in datas: 
        response = sendToAi(data)  
        invalidData(data,response,"REFUND")

# ebay-category / API_REQUIRED / 테스트 - (데이터 여러개, 한번씩만 검증)
def get_API_REQUIRED_FromEbayCategoryExcelFunction():
    datas = get_API_REQUIRED_FromEbayCategoryExcel() 
    for data in datas: 
        response = sendToAi(data)  
        invalidData(data,response,"API_REQUIRED")

# ebay-category / HUMAN_REVIEW / 테스트 - (데이터 여러개, 한번씩만 검증)
def get_HUMAN_REVIEW_FromEbayCategoryExcelFunction():
    datas = get_HUMAN_REVIEW_FromEbayCategoryExcel() 
    for data in datas: 
        response = sendToAi(data)  
        invalidData(data,response,"HUMAN_REVIEW")

check_TYPE_FromEbayCategoryExcelFunction("HUMAN_REVIEW","There still no refund!!!!! I check every day...........")