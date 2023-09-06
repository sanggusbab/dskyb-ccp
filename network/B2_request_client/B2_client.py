import httpx

# 비동기 클라이언트 생성
async def A_client(file):
    async with httpx.AsyncClient() as client:
        # 서버에 보낼 데이터 생성
        for line in file.readlines():
            data = {"number" : line}
            response = await client.post("http://localhost:8001/", json=data)
            print("POST 요청 응답:", response.json())

def run():
    import asyncio
    while True:
        with open("../B_public/example.txt", "r") as file:
            asyncio.run(A_client(file))


if __name__ == "__main__":
    run()