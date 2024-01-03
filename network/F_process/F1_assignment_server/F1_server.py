from fastapi import FastAPI
from pydantic import BaseModel
import threading
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from F_public import database
from F_public import models

engine = database.engineconn()
session = engine.sessionmaker()

app = FastAPI()

class Item(BaseModel):
    device_id: int

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

@app.post("/F1")
async def F1_server(item: Item):
    assignment_tbl = session.query(models.assignment_tbl).filter(models.assignment_tbl.device_id == item.device_id).all()

    for data in assignment_tbl:
        if data.take_yn == 'n':
            data.take_yn = 'y'
            session.commit()
            return '명령을 받았습니다.'
        else:
            return '이미 명령을 받았습니다.'
    else:
        return '가게를 찾을 수 없습니다.'

def F1_run():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)

if __name__ == "__main__":
    F1_run()
