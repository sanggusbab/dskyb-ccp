from fastapi import FastAPI
from pydantic import BaseModel
import threading
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from C_public import database #import engineconn
from C_public import models #import tbl1

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

app = FastAPI()

class Item1(BaseModel):
    task_id = int
    position_x = float
    position_y = float

class Item2(BaseModel):
    index = int
    edge_id = int
    rect_left = float
    rect_top = float
    rect_right = float
    rect_bottom = float


# 파일에 데이터를 추가하는 함수
def append_to_file(item):
    with open("../C_public/example.txt", "a") as file: # TODO: you need to change when setting server sample script
        file.write(str(item.number) + "\n")
        file.close()

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()


@app.post("/request")
async def C1_server(item: Item1): # TODO: you need to change when setting server sample script
    rect_left = item.position_x - 2
    rect_bottom = item.position_y - 2
    rect_right = item.position_x + 2
    rect_top = item.position_y + 2
    
    x1, y1, x2, y2 = rect_left, rect_bottom, rect_right, rect_top

    # 영역 안에 있는 edge를 찾는 함수
    def find_edge_in_area(edge, x1, y1, x2, y2):
        result = []
        for item in edge:
            x, y = item["x"], item["y"]
            if x1 <= x <= x2 and y1 <= y <= y2:
                result.append(item)
        return result

    # 영역 안에 있는 데이터 찾기
    result = find_edge_in_area(edge, x1, y1, x2, y2)

    # 결과 출력
    print("주변에 있는 드론 정보:")
    for item in result:
        print(f"x: {item['x']}, y: {item['y']}, value: {item['value']}")

    with file_lock:
        append_to_file(item)
    return item


def C1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    C1_run() # TODO: you need to change when setting server sample script