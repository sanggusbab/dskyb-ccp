import httpx

# 비동기 클라이언트 생성
async def main():
    async with httpx.AsyncClient() as client:
        # 서버에 보낼 데이터 생성
        data = {"name": "테스트 아이템", "description": "이 아이템은 테스트입니다."}

        # 서버의 /items/ 엔드포인트로 POST 요청을 보냅니다.
        response = await client.post("http://localhost:8000/items/", json=data)
        print("POST 요청 응답:")
        print(response.json())

if __name__ == "__main__":
    import asyncio
    while True:
        asyncio.run(main())
