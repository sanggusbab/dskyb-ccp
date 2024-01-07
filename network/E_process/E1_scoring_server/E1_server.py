from fastapi import FastAPI
from pydantic import BaseModel
import threading
from datetime import datetime

import json

#서버가 음 스코어들이 이렇게나왔으니
#이 디바이스는 이 태스크 이 디바이스는 이 태스크를 수행하렴 하고 시키는것
#D2에서 타임, 스코어, 태스크 주면 E1에서 디바이스에 할당하도록 할까요?

app = FastAPI()

class Item(BaseModel):
    expected_score: int
    expected_time: datetime
    task_subgroup_code: int


# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

# 파일에 데이터를 추가하는 함수
def append_to_file(data):
    with open("../E_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    json_data['data'].append(data)
    print(json_data)
    with open("../E_public/data.json", "w") as file: # TODO: you need to change when setting server sample script
        json.dump(json_data, file, default=str)

@app.get("/")
def root():
    return {"hello this is World Time CRUD API!!!"}

@app.post("/")
async def E1_server(item: Item): # TODO: you need to change when setting server sample script
    data = {
    "expected_score":item.expected_score, "expected_time":item.expected_time, "task_subgroup_code":item.task_subgroup_code}
    with file_lock:
        append_to_file(data)
    return item


def E1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    E1_run() # TODO: you need to change when setting server sample script