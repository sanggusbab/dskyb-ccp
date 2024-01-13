import httpx
import json
import sys, os
import time
import asyncio

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from C_public import database
from C_public import models

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

def is_available(device, task):
    available_edge = []
    for key in device:
        keys_device = set(device[key].keys())
        keys_task = set(task.keys())

        if not keys_task.issubset(keys_device):
            continue
        flag = True
        for i in task:
            x, y = task[i]
            l,r,t,b = device[key][i]
            if not(l <= x <= r and b <= y <= t):
                flag = False
        if flag:
            available_edge.append(key)
    return available_edge

def get_first_entry_from_json():
    json_file_path = '../C_public/data.json'
    try:
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
            if existing_data:
                first_entry = existing_data[0]
                remaining_entries = existing_data[1:]
                with open(json_file_path, 'w') as updated_json_file:
                    json.dump(remaining_entries, updated_json_file, default=str)
                return first_entry
            else:
                return None  # Return None if the file is empty
    except (FileNotFoundError, json.JSONDecodeError, IndexError):
        return None

async def C2_client():
    first_entry = get_first_entry_from_json()
    if first_entry:
        print("First entry from data.json:", first_entry)
    else:
        print("No entries in data.json. Pause program 5 secs")
        time.sleep(5)
        return None
    task = {}
    print(first_entry)
    data_detail = session.query(models.SubgroupDetailTbl).filter(models.SubgroupDetailTbl.task_subgroup_code == first_entry).all()
    for task_data in data_detail:
        task[task_data.motion_code]=[task_data.location_x, task_data.location_y]
    device = get_device_info()
    available_edge = is_available(device, task)

    for i in available_edge:
        data_detail = models.ScoreRequestQueueTbl(task_subgroup_code = first_entry, device_id = i)
        session.add(data_detail)
        session.commit()
        id = session.query(models.ScoreRequestQueueTbl).filter((models.ScoreRequestQueueTbl.task_subgroup_code == first_entry)&(models.ScoreRequestQueueTbl.device_id == i)).first().request_id

        async with httpx.AsyncClient() as client:
            response = await client.post("http://localhost:8002/request", json={"request_id": id})
        print("Response :", response.json())

def C2_run():
    while True:
        asyncio.run(C2_client())
        time.sleep(0.5)


if __name__ == "__main__":
    C2_run()