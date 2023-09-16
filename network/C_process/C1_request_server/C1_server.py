from fastapi import FastAPI
from pydantic import BaseModel
import threading
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from C_public import database #import engineconn
from C_public import models #import Program, Register

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

app = FastAPI()

class Item(BaseModel):
    index = int
    device_id = int
    rect_top = float
    rect_bottom = float
    rect_left = float
    rect_right = float

# 파일에 데이터를 추가하는 함수
def append_to_file(item):
    with open("../C_public/example.txt", "a") as file: # TODO: you need to change when setting server sample script
        file.write(str(item.number) + "\n")
        file.close()

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

# main http
@app.get("/", description="This is World Time CRUD API")
def root():
    return {"hello this is World Time CRUD API!!!"}


# @app.post("/request")
# async def B1_server(item: Item): # TODO: you need to change when setting server sample script
# 
#     session.add(data)
#     session.commit()
#     return 'success'

    # # 파일 접근을 Lock으로 동기화
    # item.number = item.number + 1 # TODO: you need to change when setting server sample script
    # with file_lock:
    #     append_to_file(item)
    # return item

def B1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    B1_run() # TODO: you need to change when setting server sample script

    # 데이터를 나타내는 리스트 (예제 데이터)
data = [
    {"x": 3, "y": 4, "value": "A"},
    {"x": 1, "y": 2, "value": "B"},
    {"x": 5, "y": 6, "value": "C"},
    {"x": 2, "y": 7, "value": "D"},
    {"x": 6, "y": 3, "value": "E"},
]

# 원하는 영역의 좌표 (x1, y1)에서 (x2, y2)까지
x1, y1, x2, y2 = rect_left, rect_bottom, rect_right, rect_top

# 영역 안에 있는 edge를 찾는 함수
def find_data_in_area(data, x1, y1, x2, y2):
    result = []
    for item in data:
        x, y = item["x"], item["y"]
        if x1 <= x <= x2 and y1 <= y <= y2:
            result.append(item)
    return result

# 영역 안에 있는 데이터 찾기
result = find_data_in_area(data, x1, y1, x2, y2)

# 결과 출력
print("원하는 영역 안에 있는 데이터:")
for item in result:
    print(f"x: {item['x']}, y: {item['y']}, value: {item['value']}")