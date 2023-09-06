from fastapi import FastAPI
from pydantic import BaseModel
import threading

app = FastAPI()

class Item(BaseModel):
    number: int

# 파일에 데이터를 추가하는 함수
def append_to_file(item):
    with open("../B_public/example.txt", "a") as file:
        file.write(str(item.number) + "\n")
        file.close()

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

@app.post("/")
async def B1_server(item: Item):
    # 파일 접근을 Lock으로 동기화
    item.number = item.number + 1
    with file_lock:
        append_to_file(item)
    return item

def B1run():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == "__main__":
    B1run()