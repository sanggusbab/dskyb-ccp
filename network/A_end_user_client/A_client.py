import httpx

# 비동기 클라이언트 생성
async def A_client(num):
    async with httpx.AsyncClient() as client:
        # 서버에 보낼 데이터 생성
        data = {"number" : num}
        response = await client.post("http://localhost:8000/", json=data)
        print("POST 요청 응답:", response.json())

def run():
    import asyncio
    while True:
        num = input("숫자와 입력하세요: ")
        asyncio.run(A_client(num))


if __name__ == "__main__":
    run()