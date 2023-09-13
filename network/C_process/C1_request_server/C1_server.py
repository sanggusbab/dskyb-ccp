from fastapi import FastAPI
from pydantic import BaseModel
import threading

app = FastAPI()

class Item(BaseModel):
    isnull: bool
    data: int

# 파일에 데이터를 추가하는 함수
def append_to_file(item):
    with open("../C_public/example.txt", "a") as file: # TODO: you need to change when setting server sample script
        if item.isnull:
            file.write("\n")
        else:
            file.write(str(item.data) + "\n")
        file.close()

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

@app.post("/")
async def C1_server(item: Item): # TODO: you need to change when setting server sample script
    # 파일 접근을 Lock으로 동기화
    if item.isnull:
        with file_lock:
            append_to_file(item)
        return "no data"
    else:
        item.data = item.data + 10 # TODO: you need to change when setting server sample script
        with file_lock:
            append_to_file(item)
        return item

def C1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    C1_run() # TODO: you need to change when setting server sample script