import httpx
import json
import sys, os

#다른 폴더로 분리한 파일 가져오기위함.
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from F_public import database
from F_public import models

#기본세팅
engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

my_device_id = 1

def drone_do(task):
    return task

# 비동기 클라이언트 생성
async def F2_client(): # TODO: you need to change when setting server sample script
    with open("../F_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    data_list = json_data["data"]
    if not len(data_list) == 0:
        task = data_list.pop(0)
        print(task)
        assignment_tbl = session.query(models.assignment_tbl).filter((models.assignment_tbl.device_id == my_device_id)&(models.assignment_tbl.task_subgroup_code == task)).first()
        if assignment_tbl.take_yn == 'n':
            task = drone_do(task)
            print("수행완료")
            assignment_tbl.take_yn = 'y'
            session.commit()
            async with httpx.AsyncClient() as client:
                response = await client.post("http://localhost:8005/", json={"assignment_id":assignment_tbl.index})
            print("POST 요청 응답:", response.json())
        else:print("이미 수행된 과제입니다.")
        json_data["data"] = data_list
        with open("../F_public/data.json", "w") as file:
            json.dump(json_data, file, default=str)
        
    return

def F2_run(): # TODO: you need to change when setting server sample script
    import asyncio
    while True:
        asyncio.run(F2_client()) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    F2_run() # TODO: you need to change when setting server sample script