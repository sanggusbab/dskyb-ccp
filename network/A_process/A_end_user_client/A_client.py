import httpx

# 비동기 클라이언트 생성
async def A_client(request, task_id, task_group):
    async with httpx.AsyncClient() as client:
        # 서버에 보낼 데이터 생성
        data = {
            "request": request,
            "location_x": 1.0,
            "location_y": 2.0,
            "start_time": "2023-12-13T08:30:00",
            "user_id": 1,
            "task_id": task_id,
            "task_group": task_group
        }
        response = await client.post("http://localhost:8000/", json=data)
        print("POST 요청 응답:", response.json())

def A_run():
    import asyncio
    while True:
        request = input("명령을 입력하세요: ")
        task_id = int(input("task정보를 입력하세요: "))
        task_group = int(input("그룹 정보를 입력하세요: "))
        asyncio.run(A_client(request, task_id, task_group))


if __name__ == "__main__":
    A_run()