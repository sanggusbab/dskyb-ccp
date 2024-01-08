import httpx
import json
import sys, os

#다른 폴더로 분리한 파일 가져오기위함.
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from C_public import database
from C_public import models

#기본세팅
engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

def get_device_info():
    device_detail = session.query(models.AvailableEdgeDeviceTbl).all()
    device = {}
    for device_data in device_detail:
        if device_data.device_id not in device:
            device[device_data.device_id] = {}
            device[device_data.device_id][device_data.motion_code] = [device_data.rect_left, device_data.rect_right, device_data.rect_top, device_data.rect_bottom]
        else: device[device_data.device_id][device_data.motion_code] = [device_data.rect_left, device_data.rect_right, device_data.rect_top, device_data.rect_bottom]
    return device

{1: {'1': [-2, 26.5, 10.5, 0], '2': [-4.2, 3, 10.5, 0], '3': [-15.7, 13, 3, -26.3], '5': [4.5, 12.5, 33.1, 14.5], '10': [-0.6, 6.3, 12.8, 1.4]},
2: {'1': [3.8, 25, 25, 5.7],'2': [-7.6, 1.9, 28.7, -32.1], '3': [-7.5, 30, 22.4, -30.8], '5': [-9.5, 2.9, -34.6, -46.4], '8': [-0.6, 1.7, -31.6, -49.6], '10': [-6.0, 0.5, 7.0, -11.5]},
3: {'1': [11.2, 24.7, -5.9, -18.0], '3': [9.0, 10.7, 29.2, 14.0], '4': [-8.4, 0, 5.4, -15.4], '5': [1.3, 2.4, -11.7, -19.3], '9': [-9.0, 2.1, 1.6, -14.4], '10': [-5.1, 7.5, -20.2, -29.0]},
4: {'1': [-12.3, -4.7, -32.2, -38.1], '3': [20.0, 24.9, -7.3, -25.8], '4': [6.8, 13.4, 8.9, 2.7], '5': [15.8, 23.3, -15.7, -31.2], '6': [19.0, 32.0, -1.5, -11.3], '8': [5.2, 13.7, 10.3, 9.6], '10': [2.7, 11.4, -22.8, -30.1]},
5: {'3': [18.7, 24.7, -33.3, -44.1], '4': [-2, 0.6, 21.0, -16.8], '5': [0, 16.0, 32.4, -14.4], '6': [-19.6, -11.5, 14.4, 6.8], '10': [-14.0, -12.7, 11.3, 8.7]}}

{11: {1: [-1.0, 3.0], 2: [1.0, 2.0], 3: [2.0, 2.0]},
12: {4: [-1.0, 3.0], 5: [1.0, 2.0]},
13: {1: [20.0, 20.0], 2: [1.0, 2.0], 3: [22.0, 22.0]}}


def is_available(device, task):
    available_edge = []
    for key in device: #각 디바이스별로 순회.
        keys_device = set(device[key].keys())
        keys_task = set(task.keys())
        #만약 이 device가 task의 모든 motion code를 가지고있지 않다면
        # (task의 모션코드가 이 device의 모션코드의 subset이 아니라면) 검사를 건너뛴다.
        if not keys_task.issubset(keys_device):
            #print(f"device {key}는 task{task}의 모든 모션코드를 가지지 않습니다.")
            continue
        # 이 모든 모션코드를 가지고있다면, 위치가 사각형 안인지 검사한다.
        flag = True
        for i in task: #모션코드값으로 순회
            x, y = task[i] #모션코드값으로 xy찾기
            l,r,t,b = device[key][i] #모션코드값으로 이 디바이스의 사각형찾기
            if not(l <= x <= r and b <= y <= t): #사각형 밖에있다면
                # print(f"device {key}는 모션{i}에서 {x}, {y}의 범위 바깥에 있습니다.")
                # print(f"rect {l}:{r}, {b}:{t}")
                flag = False
        if flag:
            available_edge.append(key) #이 디바이스를 추가.
    return available_edge

# 비동기 클라이언트 생성
async def C2_client(device): # TODO: you need to change when setting server sample script
    with open("../C_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    data_list = json_data["data"]
    task = {}
    if not len(data_list) == 0:
        code = data_list.pop(0)
        print(code) #서브그룹코드 출력

        #모션들 불러와서 데이터형태저장
        data_detail = session.query(models.SubgroupDetailTbl).filter(models.SubgroupDetailTbl.task_subgroup_code == code).all()
        for task_data in data_detail:
            task[task_data.motion_code]=[task_data.location_x, task_data.location_y]

        #데이터 들고 가능한 엣지 계산
        #엣지리스트만 출력하면 됨.

        available_edge = is_available(device, task)
        print(available_edge)

        for i in available_edge:
            data_detail = models.ScoreRequestQueueTbl(task_subgroup_code = code, device_id = i)
            session.add(data_detail)
            session.commit()
            id = session.query(models.ScoreRequestQueueTbl).filter((models.ScoreRequestQueueTbl.task_subgroup_code == code)&(models.ScoreRequestQueueTbl.device_id == i)).first().request_id
            print(id)

            async with httpx.AsyncClient() as client:
                response = await client.post("http://localhost:8002/", json={"request_id": id})
            print("POST 요청 응답:", response.json())

        json_data["data"] = data_list
        with open("../C_public/data.json", "w") as file:
            json.dump(json_data, file, default=str)
    return

def C2_run():
    import asyncio
    device = get_device_info()
    while True:
        asyncio.run(C2_client(device))


if __name__ == "__main__":
    C2_run()