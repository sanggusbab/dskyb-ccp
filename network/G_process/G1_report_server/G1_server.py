from fastapi import FastAPI
from pydantic import BaseModel
import threading

import json

app = FastAPI()


class Item(BaseModel):
    assignment_id: int


# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

def append_to_file(data):
    with open("../G_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    json_data['data'].append(data)
    print(json_data)
    with open("../G_public/data.json", "w") as file: # TODO: you need to change when setting server sample script
        json.dump(json_data, file, default=str)

@app.get("/")
def root():
    return {"hello this is World Time CRUD API!!!"}


@app.post("/")
async def G1_server(item: Item): # TODO: you need to change when setting server sample script
    with file_lock:
        append_to_file(item.assignment_id)
    return item


def G1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    G1_run() # TODO: you need to change when setting server sample script