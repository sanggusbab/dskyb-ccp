from fastapi import FastAPI
from pydantic import BaseModel
import threading
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from B_public import database #import engineconn
from B_public import models #import Program, Register

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

app = FastAPI()

class Item(BaseModel):
    id: int
    user_id: int
    name: str
    program: str
    teacher: str
    pay: bool

# 파일에 데이터를 추가하는 함수
def append_to_file(item):
    with open("../B_public/example.txt", "a") as file: # TODO: you need to change when setting server sample script
        file.write(str(item.number) + "\n")
        file.close()

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

# main http
@app.get("/", description="This is World Time CRUD API")
def root():
    return {"hello this is World Time CRUD API!!!"}


@app.post("/p_test")
async def B1_server(item: Item): # TODO: you need to change when setting server sample script
    #program/teacher 정보로 program 테이블 조회
    testUsers  =  session.query(models.Program).filter((models.Program.program == item.program)&(models.Program.teacher == item.teacher))

    #pay가 true라면
    if item.pay:
        data = models.Register(id = item.id, user_id = item.user_id, name = item.name, program_cd = testUsers[0].program_cd, pay = "Y")
    #pay가 false라면
    else:
        data = models.Register(id = item.id, user_id = item.user_id, name = item.name, program_cd = testUsers[0].program_cd, pay = "Y")

    session.add(data)
    session.commit()
    return 'success'

    # # 파일 접근을 Lock으로 동기화
    # item.number = item.number + 1 # TODO: you need to change when setting server sample script
    # with file_lock:
    #     append_to_file(item)
    # return item

def B1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    B1_run() # TODO: you need to change when setting server sample script