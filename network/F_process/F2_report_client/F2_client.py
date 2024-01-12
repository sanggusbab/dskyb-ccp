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

async def F2_client():
    first_entry = get_first_entry_from_json()
    if not first_entry:
        print("No entries in data.json. Pause program 5 secs")
        time.sleep(5)
        return None
    task = first_entry
    print(task)
    assignment_tbl = session.query(models.assignment_tbl).filter((models.assignment_tbl.device_id == my_device_id)&(models.assignment_tbl.task_subgroup_code == task)).first()
    if assignment_tbl.take_yn == 'n':
        task = drone_do(task)
        print("?àò?ñâ?ôÑÎ£?")
        assignment_tbl.take_yn = 'y'
        session.commit()
        async with httpx.AsyncClient() as client:
            response = await client.post("http://localhost:8005/", json={"assignment_id":assignment_tbl.index})
        print("Response:", response.json())
    else:print("?ù¥ÎØ? ?àò?ñâ?êú Í≥ºÏ†ú?ûÖ?ãà?ã§.")
    return

def F2_run():
    import asyncio
    while True:
        asyncio.run(F2_client())

if __name__ == "__main__":
    F2_run()