from fastapi import FastAPI
from pydantic import BaseModel
import threading
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from C_public import database #import engineconn
from C_public import models #import B2, C1

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

app = FastAPI()


class Item(BaseModel):
    task_subgroup_code: int

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()


@app.post("/request")
async def C1_server(item: Item): # TODO: you need to change when setting server sample script

    # 영역 안에 있는 edge를 찾는 함수
    def find_edge_in_area(devices, x, y, motion_code):
        device_ids = []
        for device in devices:  
            if (int(device.motion_code) == motion_code):
                x1 = device.rect_left
                x2 = device.rect_right
                y1 = device.rect_bottom
                y2 = device.rect_top
                if x1 <= x <= x2 and y1 <= y <= y2:
                    device_ids.append(device.device_id)
        return device_ids

    tasks = session.query(models.subgroup_detail_tbl).filter(models.subgroup_detail_tbl.task_subgroup_code == item.task_subgroup_code).all()
    devices = session.query(models.available_edge_device_tbl).all()

    for task in tasks:
        print(f"subgroup_code:{item.task_subgroup_code}, x: {task.location_x}, y: {task.location_y}")
        x = task.location_x
        y = task.location_y
        motion_code = task.motion_code
        device_ids = find_edge_in_area(devices, x, y, motion_code)


        # 결과 출력
        print(f"{motion_code}를 수행할 수 있는 드론 정보:", end='')
        if len(device_ids) == 0:
            print("null")
        else:
            for device_id in device_ids:
                print(device_id, end=', ')
                data = models.C1(
                device_id = device_id, task_subgroup_code=item.task_subgroup_code
                )
                session.add(data)
            print()
    session.commit()
    return 'success'


def C1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001) # TODO: you need to change when setting server sample script


if __name__ == "__main__":
    C1_run() # TODO: you need to change when setting server sample script