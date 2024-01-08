import httpx

# 비동기 클라이언트 생성
async def D2_client(): # TODO: you need to change when setting server sample script
    async with httpx.AsyncClient() as client:
    response = await client.post("http://localhost:8003/", json=data) # TODO: you need to change when setting server sample script
    print("POST 요청 응답:", response.json())

def D2_run(): # TODO: you need to change when setting server sample script
    import asyncio
    while True:
        asyncio.run(D2_client()) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    D2_run() # TODO: you need to change when setting server sample script