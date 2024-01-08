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


#서버가 음 스코어들이 이렇게나왔으니
#이 디바이스는 이 태스크 이 디바이스는 이 태스크를 수행하렴 하고 시키는것
#D2에서 타임, 스코어, 태스크 주면 E1에서 디바이스에 할당하도록 할까요?

def assign(score, time, task, device):
    return task, device

# 비동기 클라이언트 생성
async def E2_client(): # TODO: you need to change when setting server sample script
    with open("../E_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    data_list = json_data["data"]
    if not len(data_list) == 0:
        request_id = data_list.pop(0)
        print(request_id)
        score_tbl = session.query(models.score_tbl).filter(models.score_tbl.request_id == request_id).first()
        request_queue_tbl = session.query(models.score_request_queue_tbl).filter(models.score_request_queue_tbl.request_id == request_id).first()
        print(score_tbl.expected_score)
        subgroup_code, device_id = assign(score_tbl.expected_score, score_tbl.expected_time, request_queue_tbl.task_subgroup_code, request_queue_tbl.device_id)
        datas = models.assignment_tbl(
        device_id = device_id, task_subgroup_code = subgroup_code, take_yn = 'n'
        )
        session.add(datas)
        session.commit()
        async with httpx.AsyncClient() as client:
            response = await client.post("http://localhost:8004/", json={"device_id":device_id, "task_subgroup_code": subgroup_code})
        print("POST 요청 응답:", response.json())
        json_data["data"] = data_list
        with open("../E_public/data.json", "w") as file:
            json.dump(json_data, file, default=str)
    return

def E2_run(): # TODO: you need to change when setting server sample script
    import asyncio
    while True:
        asyncio.run(E2_client()) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    E2_run() # TODO: you need to change when setting server sample script