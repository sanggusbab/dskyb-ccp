from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# 요청 데이터를 처리하기 위한 Pydantic 모델 정의
class Item(BaseModel):
    key1: str
    key2: str

# POST 요청을 처리하는 핸들러
@app.post("/submit")
async def submit(item: Item):
    # 요청으로 받은 데이터 처리
    result = {
        "message": "POST 요청이 성공적으로 처리되었습니다.",
        "received_data": item.dict()
    }
    return result
