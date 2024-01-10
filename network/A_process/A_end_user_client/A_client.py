import httpx
from datetime import datetime
# 비동기 클라이언트 생성
async def A_client(request, location_x, location_y, start_time, user_id, task_id, task_group):
    async with httpx.AsyncClient() as client:
        # 서버에 보낼 데이터 생성
        data = {
            "request": request,
            "location_x": location_x,
            "location_y": location_y,
            "start_time": start_time,
            "user_id": user_id,
            "task_id": task_id,
            "task_group": task_group
        }
        response = await client.post("http://localhost:8000/", json=data)
        print("POST 요청 응답:", response.json())

def A_run():
    import asyncio
    while True:
        print("------------------------")
        request = input("명령을 입력하세요: ")
        location_x = float(input("location_x: "))
        location_y = float(input("location_y: "))
        current_time = datetime.now()
        start_time = current_time.strftime("%Y-%m-%dT%H:%M:%S")
        user_id = int(input("user_id: "))
        task_id = int(input("task정보를 입력하세요: "))
        task_group = int(input("그룹 정보를 입력하세요: "))
        asyncio.run(A_client(request, location_x, location_y, start_time, user_id, task_id, task_group))


if __name__ == "__main__":
    A_run()
import httpx

# 鍮꾨룞湲? ?겢?씪?씠?뼵?듃 ?깮?꽦
async def A_client(request, task_id, task_group):
    async with httpx.AsyncClient() as client:
        # ?꽌踰꾩뿉 蹂대궪 ?뜲?씠?꽣 ?깮?꽦
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
        print("POST ?슂泥? ?쓳?떟:", response.json())

def A_run():
    import asyncio
    while True:
        request = input("紐낅졊?쓣 ?엯?젰?븯?꽭?슂: ")
        task_id = int(input("task?젙蹂대?? ?엯?젰?븯?꽭?슂: "))
        task_group = int(input("洹몃９ ?젙蹂대?? ?엯?젰?븯?꽭?슂: "))
        asyncio.run(A_client(request, task_id, task_group))


if __name__ == "__main__":
    A_run()