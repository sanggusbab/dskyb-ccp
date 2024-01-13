import httpx
import json
import sys, os
from datetime import datetime, timedelta
import time
import random
import asyncio

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from D_public import database
from D_public import models

engine = database.engineconn()
session = engine.sessionmaker()
conn = engine.connection()

def calc_expected_spec():
    expected_score = int(random.random() * 100)
    expected_time = (datetime.min + timedelta(seconds=random.randint(5, 30))).time().strftime("%H:%M:%S")
    return expected_score, expected_time

def get_first_entry_from_json():
    json_file_path = '../D_public/data.json'
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

async def D2_client():
    first_entry = get_first_entry_from_json()
    if not first_entry:
        print("No entries in data.json. Pause program 3 secs")
        time.sleep(3)
        return None
    expected_score, expected_time = calc_expected_spec()
    score_data = models.score_tbl(
        expected_score = expected_score,
        expected_time = expected_time,
        request_id = first_entry
    )
    session.add(score_data)
    session.commit()
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8003/request", json={"request_id":int(first_entry)})
    print("Response:", response.json())
    return

def D2_run():
    while True:
        asyncio.run(D2_client())

if __name__ == "__main__":
    D2_run()