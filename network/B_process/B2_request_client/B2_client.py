import httpx
import json
import sys, os
import time
import asyncio

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from B_public import database
from B_public import models

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

subgroup_code = 0
task_id = 0

def get_first_entry_from_json():
    json_file_path = '../B_public/data.json'
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

async def B2_client():
    global subgroup_code
    global task_id
    first_entry = get_first_entry_from_json()
    if first_entry:
        print("First entry from data.json:", first_entry)
    else:
        print("No entries in data.json. Pause program 5 secs")
        time.sleep(5)
        return None
    for i in range(0, 6):
        data_detail = models.SubgroupDetailTbl(
            task_subgroup_code = subgroup_code + int(i/3),
            location_x = first_entry[f"Location{int(i/3)+1}_x"],
            location_y = first_entry[f"Location{int(i/3)+1}_y"],
            motion_code = i % 3 +1, # Moveto, Landing, Takeoff
            sequence = i,
            requested_start_time=first_entry["currentTime"])
        session.add(data_detail)
        if int(i%3) ==0:
            async with httpx.AsyncClient() as client:
                response = await client.post("http://localhost:8001/request", json={"task_subgroup_code": subgroup_code + int(i/3)})
                print("Response:", response.json())
            subgroup_info_data=models.SubgroupInfoTbl(
                task_id=task_id,
                task_group=task_id,
                task_subgroup_code=subgroup_code + int(i/3),
                user_id=first_entry["userId"])
            session.add(subgroup_info_data)
        session.commit()
    subgroup_code = subgroup_code + 2
    task_id = task_id +1
    return

def B2_run():
    while True:
        asyncio.run(B2_client())
        time.sleep(0.5)


if __name__ == "__main__":
    B2_run()