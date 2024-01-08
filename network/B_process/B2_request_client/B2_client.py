import httpx
import json
import sys, os

#다른 폴더로 분리한 파일 가져오기위함.
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from B_public import database
from B_public import models

#기본세팅
engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

subgroup_code = 0

def parse(request):
    requests = request.split(",")
    motion = ["Takeoff","Landing","ForwardFlight","BackwardFlight","SidewaysMovement","Ascend","Descend","Rotation","Hovering","SpeedAdjustment","AltitudeHolding","ReturntoHome","Pathfinding","Post-MissionHolding","ObjectTracking"]
    result_ids = []
    for action in requests:
        if action in motion:
            action_id = motion.index(action)+1
            result_ids.append(action_id)
    return result_ids

async def B2_client():
    with open("../B_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    data_list = json_data["data"]
    if not len(data_list) == 0:
        data = data_list.pop(0)
        global subgroup_code
        subgroup_code+= 1
        motion_codes = parse(data["request"])
        for i, code in enumerate(motion_codes):
            print(code)
            subgroup_detail_data= {"task_subgroup_code": subgroup_code}
            data_detail = models.SubgroupDetailTbl(task_subgroup_code = subgroup_code, location_x = data["location_x"], location_y = data["location_y"], motion_code = code, sequence =i+1, requested_start_time=data["start_time"])
            session.add(data_detail)
        async with httpx.AsyncClient() as client:
            response = await client.post("http://localhost:8001/request", json=subgroup_detail_data)
            print("POST 요청 응답:", response.json())
        subgroup_info_data=models.SubgroupInfoTbl(task_id  = data["task_id"], task_group = data["task_group"], task_subgroup_code = subgroup_code, user_id = data["user_id"])
        session.add(subgroup_info_data)
        session.commit()
        json_data["data"] = data_list
        with open("../B_public/data.json", "w") as file:
            json.dump(json_data, file, default=str)
    return


def B2_run():
    import asyncio
    while True:
        asyncio.run(B2_client())


if __name__ == "__main__":
    B2_run()