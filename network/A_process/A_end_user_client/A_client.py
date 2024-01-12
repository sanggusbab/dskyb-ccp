import httpx
from datetime import datetime

async def A_client(request, location_x, location_y, start_time, user_id, task_id, task_group):
    async with httpx.AsyncClient() as client:
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
        print("Response:", response.json())

def A_run():
    import asyncio
    while True:
        print("------------------------")
        request = input("Enter the request: ")
        location_x = float(input("location_x: "))
        location_y = float(input("location_y: "))
        current_time = datetime.now()
        start_time = current_time.strftime("%Y-%m-%dT%H:%M:%S")
        user_id = int(input("user_id: "))
        task_id = int(input("Enter the task_id: "))
        task_group = int(input("Enter the task_group: "))
        asyncio.run(A_client(request, location_x, location_y, start_time, user_id, task_id, task_group))


if __name__ == "__main__":
    A_run()