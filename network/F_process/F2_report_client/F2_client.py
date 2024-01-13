import httpx
import json
import sys, os
import time
import asyncio

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from F_public import database
from F_public import models

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

my_device_id = 1

def drone_do(task):
    return task

def get_first_entry_from_json():
    json_file_path = '../F_public/data.json'
    try:
        with open(json_file_path, 'r') as json_file:
            existing_data = json.load(json_file)
            if existing_data:
                first_entry = existing_data[0]
                print(first_entry)
                # Remove the first entry from the JSON file
                remaining_entries = existing_data[1:]
                with open(json_file_path, 'w') as updated_json_file:
                    json.dump(remaining_entries, updated_json_file, default=str)
                return first_entry
            else:
                return None  # Return None if the file is empty
    except (FileNotFoundError, json.JSONDecodeError, IndexError):
        return None


async def F2_client():
    first_entry = get_first_entry_from_json()
    if not first_entry:
        print("No entries in data.json. Pause program 3 secs")
        time.sleep(3)
        return None
    subgroup_detail_tbl1 = session.query(models.subgroup_detail_tbl).filter((models.subgroup_detail_tbl.task_subgroup_code == first_entry["task_subgroup_code"])).first()
    subgroup_detail_tbl2 = session.query(models.subgroup_detail_tbl).filter((models.subgroup_detail_tbl.task_subgroup_code == (first_entry["task_subgroup_code"]+1))).first()
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8005/request",json={"device_id":first_entry["device_id"], "Location1_x":subgroup_detail_tbl1.location_x,"Location1_y": subgroup_detail_tbl1.location_y, "Location2_x":subgroup_detail_tbl2.location_x,"Location2_y": subgroup_detail_tbl2.location_y})
    print("Response:", response.json())
    session.commit()
    return

if __name__ == "__main__":
    while True:
        asyncio.run(F2_client())
        time.sleep(3)