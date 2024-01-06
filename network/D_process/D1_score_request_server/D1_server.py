from fastapi import FastAPI
from pydantic import BaseModel
import threading
import sys, os
# import time
# from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from D_public import database #import engineconn
from D_public import models #import tbl

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

app = FastAPI()


class Item(BaseModel):
    request_id: int


# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

@app.post("/")
async def D1_server(item: Item): # TODO: you need to change when setting server sample script
    # 파일 접근을 Lock으로 동기화
    # item.number = item.number + 100 # TODO: you need to change when setting server sample script
    # with file_lock:
    #     append_to_file(item)
    return item

@app.post("/D1")
async def D1_server(item: Item): # TODO: you need to change when setting server sample script

    task_subgroup_code = session.query(models.score_request_queue_tbl).filter(models.score_request_queue_tbl.request_id == item.request_id)[0].task_subgroup_code
    detail_tbl = session.query(models.subgroup_detail_tbl).filter(models.subgroup_detail_tbl.task_subgroup_code == task_subgroup_code).all()

    for data in detail_tbl:

        expected_score = data.motion_code + data.sequence # 테스트값
        expected_time  = data.requested_start_time # 테스트값

        datas = models.score_tbl(
        expected_score = expected_score, expected_time = expected_time, request_id = item.request_id
        )
        session.add(datas)
        session.commit()
        return 'success'

    
def D1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    D1_run() # TODO: you need to change when setting server sample scripts