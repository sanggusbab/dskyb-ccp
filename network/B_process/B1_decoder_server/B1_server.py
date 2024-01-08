from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import threading

import json

app = FastAPI()

class Item(BaseModel):
    request: str
    location_x: float
    location_y: float
    start_time: datetime
    user_id: int
    task_id: int
    task_group: int

# 파일에 데이터를 추가하는 함수
def append_to_file(data):
    with open("../B_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    json_data['data'].append(data)
    print(json_data)
    with open("../B_public/data.json", "w") as file: # TODO: you need to change when setting server sample script
        json.dump(json_data, file, default=str)

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

@app.get("/")
def root():
    return {"hello this is World Time CRUD API!!!"}


@app.post("/")
async def B1_server(item: Item): # TODO: you need to change when setting server sample script
    data = {"request":item.request, "location_x":item.location_x, "location_y":item.location_y, "start_time":item.start_time, "user_id":item.user_id, "task_id":item.task_id, "task_group":item.task_group}
    with file_lock:
        append_to_file(data)
    return item

def B1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    B1_run() # TODO: you need to change when setting server sample script