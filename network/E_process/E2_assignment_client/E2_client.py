import httpx
import json
import sys, os

#다른 폴더로 분리한 파일 가져오기위함.
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from E_public import database
from E_public import models

#기본세팅
engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()


# 비동기 클라이언트 생성
async def E2_client(): # TODO: you need to change when setting server sample script
    with open("../C_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    data_list = json_data["data"]
    if not len(data_list) == 0:
        data = data_list.pop(0)
        print(data) #서브그룹코드 출력
        json_data["data"] = data_list
        with open("../C_public/data.json", "w") as file:
            json.dump(json_data, file, default=str)
    return

def E2_run(): # TODO: you need to change when setting server sample script
    import asyncio
    while True:
        asyncio.run(E2_client()) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    E2_run() # TODO: you need to change when setting server sample script