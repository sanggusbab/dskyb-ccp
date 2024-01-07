import httpx
import json
import sys, os
from datetime import datetime

#다른 폴더로 분리한 파일 가져오기위함.
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from D_public import database
from D_public import models

#기본세팅
engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

def calc_expected_spec(data):
    expected_score = 0
    for detail in data:
        expected_score += detail.motion_code + detail.sequence # 테스트값
        expected_time  = detail.requested_start_time # 테스트값
    return expected_score, expected_time

# 비동기 클라이언트 생성
async def D2_client(): # TODO: you need to change when setting server sample script
    with open("../D_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    data_list = json_data["data"]
    if not len(data_list) == 0:
        id = data_list.pop(0)
        print(id) #리퀘스트 id 출력

        code = session.query(models.score_request_queue_tbl).filter(models.score_request_queue_tbl.request_id == id)[0].task_subgroup_code
        detail_tbl = session.query(models.subgroup_detail_tbl).filter(models.subgroup_detail_tbl.task_subgroup_code == code).all()
        expected_score, expected_time = calc_expected_spec(detail_tbl)
        score_data = models.score_tbl(
        expected_score = expected_score, expected_time = expected_time, request_id = id
        )
        session.add(score_data)
        session.commit()
        post_data = {
        "expected_score":expected_score, "expected_time":expected_time.isoformat(), "task_subgroup_code":code
        }
        async with httpx.AsyncClient() as client:
            response = await client.post("http://localhost:8003/", json=post_data)
        print("POST 요청 응답:", response.json())
        json_data["data"] = data_list
        with open("../D_public/data.json", "w") as file:
            json.dump(json_data, file, default=str)
    return

def D2_run(): # TODO: you need to change when setting server sample script
    import asyncio
    while True:
        asyncio.run(D2_client()) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    D2_run() # TODO: you need to change when setting server sample script