import httpx

# 비동기 클라이언트 생성
async def C2_client(): # TODO: you need to change when setting server sample script
    data = {"request_id":4}
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8002/D1", json=data) # TODO: you need to change when setting server sample script
        print("POST request :", response.json())

def C2_run(): # TODO: you need to change when setting server sample script
    import asyncio
    # while True:
    asyncio.run(C2_client()) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    C2_run() # TODO: you need to change when setting server sample script