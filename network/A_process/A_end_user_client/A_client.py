import httpx

# 비동기 클라이언트 생성
async def A_client(request, user_id):
    async with httpx.AsyncClient() as client:
        # 서버에 보낼 데이터 생성
        data = {
            "request": request,
            "location_x": 1.0,
            "location_y": 2.0,
            "start_time": "2023-12-13T08:30:00",
            "user_id": user_id
        }
        response = await client.post("http://localhost:8000/", json=data)
        print("POST 요청 응답:", response.json())

def A_run():
    import asyncio
    while True:
        request = input("명령을 입력하세요: ")
        user_id = int(input("숫자를 입력하세요: "))
        asyncio.run(A_client(request, user_id))


if __name__ == "__main__":
    A_run()