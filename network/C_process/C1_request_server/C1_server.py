from urllib import request
from fastapi import FastAPI
from pydantic import BaseModel
import threading
import sys, os

#다른 폴더로 분리한 파일 가져오기위함.
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from C_public import database
from C_public import models

#기본세팅
engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

app = FastAPI()

class Item(BaseModel):
    task_subgroup_code: int

# 파일 접근을 동기화하기 위한 Lock 객체 생성
file_lock = threading.Lock()

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


@app.get("/", description="This is World Time CRUD API")
def root():
    return {"hello this is World Time CRUD API!!!"}

# def find_device(requested_motions, loc_xs, loc_ys, device_ids, available_motions, lefts, rights, tops, bottoms):
#     for i in len(device_ids):
#     if all(action in actions for action in motions):
#         devices_capable.append(device)

@app.post("/request")
async def C1_server(item: Item): # TODO: you need to change when setting server sample script
    print(item.task_subgroup_code)
    # tasks = session.query(models.SubgroupDetailTbl).filter(models.SubgroupDetailTbl.task_subgroup_code == item.task_subgroup_code).all()
    # requested_motions, loc_xs, loc_ys = [],[],[]
    # for task in tasks:
    #     requested_motions.append(task.motion_code)
    #     loc_xs.append(task.location_x)
    #     loc_ys.append(task.location_y)

    # devices = session.query(models.AvailableEdgeDeviceTbl).all()

    # device_actions = {}
    # for item in devices:
    #     device_id = item.device_id
    #     available_motion = item.motion_code
    #     left = item.rect_left
    #     right = item.rect_right
    #     top = item.rect_top
    #     bottom = item.rect_bottm
    #     if device_id not in device_actions:
    #         device_actions[device_id] = set()
    #     # 값을 추가할 때는 update() 메서드를 사용합니다.
    #     device_actions[device_id].update([available_motion, left, right, top, bottom])

    # find_device()
    # for motion in motions:
    #     print(f"subgroup_code:{item.task_subgroup_code}, x: {motion.location_x}, y: {motion.location_y}")
    #     x = motion.location_x
    #     y = motion.location_y
    #     motion_code = motion.motion_code
    #     device_ids = find_edge_in_area(devices, x, y, motion_code)

        #서브그룹이 갖고있는 모든 모션코드를 수행할 수 있는 드론을 찾아야함.
        #1. 기능에 모든 모션코드를 갖고있는가?
        #2. 그것들이 전부 범위 안에 있는가?
        
        # # 결과 출력
        # print(f"{motion_code}를 수행할 수 있는 드론 정보:", end='')
        # if len(device_ids) == 0:
        #     print("null")
        # else:
        #     for device_id in device_ids:
        #         print(device_id, end=', ')
        #         # data = models.ScoreRequestQueueTbl(
        #         # device_id = device_id, task_subgroup_code=item.task_subgroup_code
        #         # )
        #         # session.add(data)
        #     print()
        
    session.commit()
    return 'success'


def C1_run(): # TODO: you need to change when setting server sample script
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001) # TODO: you need to change when setting server sample script

if __name__ == "__main__":
    C1_run() # TODO: you need to change when setting server sample script