import requests

# FastAPI 서버의 엔드포인트 URL
url = "http://서버주소:포트번호/엔드포인트"

# 보낼 데이터 (JSON 형식)
data = {
    "key1": "value1",
    "key2": "value2"
}

# POST 요청 보내기
response = requests.post(url, json=data)

# 서버에서 받은 응답 확인
if response.status_code == 200:
    print("요청이 성공적으로 처리되었습니다.")
    print("서버 응답:", response.json())
else:
    print("요청이 실패하였습니다.")
    print("오류 코드:", response.status_code)
    print("오류 내용:", response.text)
