import httpx
import json
import sys, os
import time
import asyncio

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from E_public import database
from E_public import models

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

def assign(score_tbl_list, score_request_queue_list):
    score = 0
    index = 0
    for i, score_tbl in enumerate(score_tbl_list):
        print(score_tbl.expected_score)
        if score <= score_tbl.expected_score:
            score = score_tbl.expected_score
            index = i
    return score_request_queue_list[index].task_subgroup_code, score_request_queue_list[index].device_id

def get_first_entry_from_json():
    json_file_path = '../E_public/data.json'
    try:
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
            if existing_data:
                first_entry = existing_data[0]
                # Remove the first entry from the JSON file
                remaining_entries = existing_data[1:]
                with open(json_file_path, 'w') as updated_json_file:
                    json.dump(remaining_entries, updated_json_file, default=str)
                return first_entry
            else:
                return None  # Return None if the file is empty
    except (FileNotFoundError, json.JSONDecodeError, IndexError):
        return None
    
async def E2_client():
    first_entry = get_first_entry_from_json()
    if not first_entry:
        print("No entries in data.json. Pause program 3 secs")
        time.sleep(3)
        return None

    score_request_queue = session.query(models.score_request_queue_tbl).filter(models.score_request_queue_tbl.request_id == first_entry).first()
    if score_request_queue is None:
        print("No score_request_queue found. Pause program 3 secs")
        time.sleep(3)
        return None

    if score_request_queue.task_subgroup_code % 2 == 0:
        score_request_queue_list = session.query(models.score_request_queue_tbl).filter(models.score_request_queue_tbl.task_subgroup_code == score_request_queue.task_subgroup_code).all()
        score_tbl_list = []
        for score_request in score_request_queue_list:
            score_tbl_list.extend(
                session.query(models.score_tbl).filter(
                    models.score_tbl.request_id == score_request.request_id
                ).all()
            )
        for i in range(len(score_tbl_list)-1):
            get_first_entry_from_json()
        return

    time.sleep(8)
    score_request_queue_list = session.query(models.score_request_queue_tbl).filter(models.score_request_queue_tbl.task_subgroup_code == score_request_queue.task_subgroup_code).all()
    score_tbl_list = []
    for score_request in score_request_queue_list:
        score_tbl_list.extend(
            session.query(models.score_tbl).filter(
                models.score_tbl.request_id == score_request.request_id
            ).all()
        )
    for i in range(len(score_tbl_list)-1):
        get_first_entry_from_json()
    subgroup_code, device_id = assign(score_tbl_list, score_request_queue_list)
    datas = models.assignment_tbl(
        device_id=device_id,
        task_subgroup_code=subgroup_code,
        take_yn='n'
    )
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8004/request", json={"device_id":device_id, "task_subgroup_code": subgroup_code})
    if response.json() != False:
        print("Response:", response.json())
        session.add(datas)
        session.commit()
    return

def E2_run():
    while True:
        asyncio.run(E2_client())

if __name__ == "__main__":
    E2_run()
