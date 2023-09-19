from fastapi import FastAPI
from pydantic import BaseModel
import threading
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from C_public import database #import engineconn
from C_public import models #import tbl

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

app = FastAPI()


class Item(BaseModel):
    task_id = int
    position_x = float
    position_y = float


# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()


@app.post("/request")
async def C1_server(item: Item): # TODO: you need to change when setting server sample script

    # edge 좌표 정보
    edge = [
        {"x": 1, "y": 4, "value": "A"},
        {"x": 5, "y": 5, "value": "B"},
        {"x": 1, "y": 1, "value": "C"},
        {"x": 2, "y": -7, "value": "D"},
        {"x": -6, "y": 3, "value": "E"},
    ]

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

    data = models.edge(edge_id = item.value, edge_x = item.x, edge_y = item.y)

    session.add(data)
    session.commit()
    return 'success'


def C1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    C1_run() # TODO: you need to change when setting server sample script