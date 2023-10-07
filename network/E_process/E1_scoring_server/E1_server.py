from fastapi import FastAPI
from pydantic import BaseModel
from datetime import time

import threading
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from E_public import database #import engineconn
from E_public import models #import tbl

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

app = FastAPI()


class Item(BaseModel):


# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

@app.post("/E1_server")
async def E1_server(item: Item): # TODO: you need to change when setting server sample script

    response = session.query(models.score_request_queue_tbl).filter(models.score_request_queue_tbl.request_id == item.request_id)
    device_id = response[0].device_id
    task_subgroup_code = response[0].task_subgroup_code

    response1 = session.query(models.subgroup_detail_tbl).filter(models.subgroup_detail_tbl.task_subgroup_code == task_subgroup_code)
    location_x = response1[0].location_x
    location_y = response1[0].location_y
    motion_code = response1[0].motion_code
    sequence = response1[0].sequence
    requested_start_time = response1[0].requested_start_time
    insrt_ts = response1[0].insrt_ts
    updt_ts = response1[0].updt_ts
    
    expected_score = location_x*10 + location_y*10 + motion_code + sequence
    expected_time = time(15, 30, 0)


    data = models.score_tbl(
    expected_score = expected_score, expected_time = expected_time, request_id = item.request_id
    )
    session.add(data)
    session.commit()
    return 'success'


def E1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    E1_run() # TODO: you need to change when setting server sample script