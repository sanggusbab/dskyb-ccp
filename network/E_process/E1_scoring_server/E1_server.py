from fastapi import FastAPI
from pydantic import BaseModel
import threading
import sys, os
# import time
# from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from E_public import database #import engineconn
from E_public import models #import tbl

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

app = FastAPI()


class Item(BaseModel):
    device_id: int


# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()


@app.post("/E1")
async def E1_server(item: Item): # TODO: you need to change when setting server sample script

    score_request_queue_tbl = session.query(models.score_request_queue_tbl).filter(models.score_request_queue_tbl.device_id == item.device_id).all()

    for data in score_request_queue_tbl:

        expected_score = session.query(models.score_tbl).filter(models.score_tbl.request_id == data.request_id)[0].expected_score
        expected_time = session.query(models.score_tbl).filter(models.score_tbl.request_id == data.request_id)[0].expected_time
        task_id = session.query(models.subgroup_info_tbl).filter(models.subgroup_info_tbl.task_subgroup_code == data.task_subgroup_code)[0].task_id
        task_group = session.query(models.subgroup_info_tbl).filter(models.subgroup_info_tbl.task_subgroup_code == data.task_subgroup_code)[0].task_group
    
        print(
            expected_score,
            expected_time,
            task_id,
            task_group
        )

        take_yn = 'y'

        datas = models.assignment_tbl(
        device_id = item.device_id, task_subgroup_code = data.task_subgroup_code, take_yn = take_yn
        )
        session.add(datas)
        session.commit()
        return 'success'








def E1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    E1_run() # TODO: you need to change when setting server sample script