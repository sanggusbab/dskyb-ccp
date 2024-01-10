import httpx
import json
import sys, os

#다른 폴더로 분리한 파일 가져오기위함.
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from G_public import database
from G_public import models

#기본세팅
engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

def ai_adjustment(l, r, t, b):
    l -=1
    r +=1
    t +=2
    b -=2
    return l, r, t, b


# 비동기 클라이언트 생성
async def G2_client(): # TODO: you need to change when setting server sample script
    with open("../G_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    data_list = json_data["data"]
    if not len(data_list) == 0:
        assignment_id = data_list.pop(0)
        print(assignment_id)
        assignment_tbl = session.query(models.assignment_tbl).filter(models.assignment_tbl.index == assignment_id).first()
        device_id = assignment_tbl.device_id
        subgroup_code = assignment_tbl.task_subgroup_code
        motions = session.query(models.subgroup_detail_tbl).filter(models.subgroup_detail_tbl.task_subgroup_code == subgroup_code).all()
        for motion_code in motions:
            edge_tbl = session.query(models.available_edge_device_tbl).filter((models.available_edge_device_tbl.motion_code == motion_code.motion_code)&(models.available_edge_device_tbl.device_id == device_id)).first()
            edge_tbl.rect_left, edge_tbl.rect_right, edge_tbl.rect_top, edge_tbl.rect_bottom = ai_adjustment(edge_tbl.rect_left, edge_tbl.rect_right, edge_tbl.rect_top, edge_tbl.rect_bottom)
            session.commit()
        json_data["data"] = data_list
        with open("../G_public/data.json", "w") as file:
            json.dump(json_data, file, default=str)
    return


def G2_run(): # TODO: you need to change when setting server sample script
    import asyncio
    while True:
        asyncio.run(G2_client()) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    G2_run() # TODO: you need to change when setting server sample script