from fastapi import FastAPI
from pydantic import BaseModel
import threading
import sys, os
# import time
# from datetime import datetime

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from G_public import database #import engineconn
from G_public import models #import tbl

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

app = FastAPI()


class Item(BaseModel):
    index: int


# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()


@app.post("/G1")
async def E1_server(item: Item): # TODO: you need to change when setting server sample script

    available_edge_device_tbl = session.query(models.available_edge_device_tbl).filter(models.available_edge_device_tbl.index == item.index).all()

    for data in available_edge_device_tbl:
        if data:

            data.rect_left = data.rect_left + 1        # AI 로직
            data.rect_top = data.rect_top + 2          # AI 로직
            data.rect_right = data.rect_right - 1      # AI 로직
            data.rect_bottom = data.rect_bottom - 2    # AI 로직

            session.commit()
            return 'success'


def G1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    G1_run() # TODO: you need to change when setting server sample script