from fastapi import FastAPI
from pydantic import BaseModel
import threading

import json

app = FastAPI()

my_device_id = 1

class Item(BaseModel):
    device_id: int
    task_subgroup_code: int

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

def append_to_file(data):
    with open("../F_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    json_data['data'].append(data)
    print(json_data)
    with open("../F_public/data.json", "w") as file: # TODO: you need to change when setting server sample script
        json.dump(json_data, file, default=str)

@app.get("/")
def root():
    return {"hello this is World Time CRUD API!!!"}


@app.post("/")
async def E1_server(item: Item): # TODO: you need to change when setting server sample script
    if item.device_id == my_device_id:
        with file_lock:
            append_to_file(item.task_subgroup_code)
        return item

def F1_run():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)

if __name__ == "__main__":
    F1_run()
