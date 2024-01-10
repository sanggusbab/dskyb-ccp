from fastapi import FastAPI
from pydantic import BaseModel
import threading

import json

app = FastAPI()

class Item(BaseModel):
    task_subgroup_code: int

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

# 파일에 데이터를 추가하는 함수
def append_to_file(data):
    with open("../C_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    json_data['data'].append(data)
    print(json_data)
    with open("../C_public/data.json", "w") as file: # TODO: you need to change when setting server sample script
        json.dump(json_data, file, default=str)


@app.get("/", description="This is World Time CRUD API")
def root():
    return {"hello this is World Time CRUD API!!!"}


@app.post("/request")
async def C1_server(item: Item): # TODO: you need to change when setting server sample script
    append_to_file(item.task_subgroup_code)
    return item


def C1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001) # TODO: you need to change when setting server sample script

if __name__ == "__main__":
    C1_run() # TODO: you need to change when setting server sample script