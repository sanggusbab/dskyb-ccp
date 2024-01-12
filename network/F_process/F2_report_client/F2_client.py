import httpx
import json
import sys, os
import time
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
                first_entry = existing_data[0].get("request_id")
                # Remove the first entry from the JSON file
                remaining_entries = existing_data[1:]
                with open(json_file_path, 'w') as updated_json_file:
                    json.dump(remaining_entries, updated_json_file, indent=2, default=str)
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
    print(first_entry)
    assignment_tbl = session.query(models.assignment_tbl).filter((models.assignment_tbl.task_subgroup_code == first_entry.task_subgroup_code)).first()
    if assignment_tbl.take_yn == 'n':
        first_entry = drone_do(first_entry)
        assignment_tbl.take_yn = 'y'
        session.commit()
        async with httpx.AsyncClient() as client:
            response = await client.post("http://localhost:8005/", json={"assignment_id":assignment_tbl.index})
        print("Response:", response.json())
    return

def F2_run():
    import asyncio
    while True:
        asyncio.run(F2_client())
        time.sleep(0.5)

if __name__ == "__main__":
    F2_run()