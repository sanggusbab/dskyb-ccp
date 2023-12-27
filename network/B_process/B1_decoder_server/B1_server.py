from msilib import sequence
from urllib import request
from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
import threading
import sys, os

import random

#다른 폴더로 분리한 파일 가져오기위함.
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from B_public import database
from B_public import models

#기본세팅
engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

app = FastAPI()

class Item(BaseModel):
    request: str
    location_x: float
    location_y: float
    start_time: datetime
    user_id: int

# {
#     "request": "ForwardFlight,Post-MissionHolding,SpeedAdjustment,Descend,ObjectTracking,BackwardFlight,Descend,Takeoff,Pathfinding,Post-MissionHolding",
#     "location_x": 1.0,
#     "location_y": 2.0,
#     "start_time": "2023-12-13T08:30:00",
#     "user_id": 1
# }

def decode_nl(item): #삼중 배열로 된 item 목록을 리턴. 첫째수준: 그룹/둘째수준: 서브그룹/ 셋째수준: 각 모션
    items = item.split(",")
    grouped_items = []
    while items:
        # 만약 남은 아이템이 5개 이하라면 그대로 그룹으로 묶습니다.
        if len(items) <= 5:
            num_words = len(items)
        else:
            num_words = random.randint(2, 5)  # 2~5개의 단어로 묶음

        # num_words 만큼의 아이템을 묶어서 group 변수에 저장합니다.
        group = items[:num_words]
        tempgroup = []

        while group:
            # 만약 그룹에 남은 아이템이 2개 이하라면 그대로 묶습니다.
            if len(group) <= 2:
                rn = len(group)
            else:
                rn = random.randint(1, min(2, len(group)))  # 1~2개의 단어로 묶음

            # rn 개수만큼의 아이템을 묶어서 subgroup 변수에 저장합니다.
            subgroup = group[:rn]
            tempgroup.append(subgroup)
            group = group[rn:]  # 선택한 단어들을 원본 그룹에서 제거

        # 묶인 단어들을 grouped_items 리스트에 추가합니다.
        grouped_items.append(tempgroup)
        items = items[num_words:]  # 선택한 단어들을 원본 리스트에서 제거
    return grouped_items

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

# main http
@app.get("/", description="This is World Time CRUD API")
def root():
    return {"hello this is World Time CRUD API!!!"}

class IndexHolder:
    def __init__(self):
        self.index = 0

index_holder = IndexHolder()

@app.post("/natural_request")
async def decode(item: Item):
    global index_holder
    grouped_items = decode_nl(item.request)
    for i, group in enumerate(grouped_items):#그룹단계
        for j, subgroup in enumerate(group):#서브그룹단계
            data_info = models.SubgroupInfoTbl(task_id = index_holder.index, user_id = item.user_id, task_group = i, task_subgroup_code = index_holder.index*i+j)
            for k, request in enumerate(subgroup):#모션단계
                motion_code  =  session.query(models.MotionCodeInfoTbl).filter((models.MotionCodeInfoTbl.description == request))[0].motion_code
                data_detail = models.SubgroupDetailTbl(task_subgroup_code = index_holder.index*i+j, location_x = item.location_x, location_y = item.location_y, motion_code = motion_code, sequence = k, requested_start_time = item.start_time)
                session.add(data_detail)
            session.add(data_info)
    session.commit()
    index_holder.index += 1
    return "success"


def B1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    B1_run() # TODO: you need to change when setting server sample script