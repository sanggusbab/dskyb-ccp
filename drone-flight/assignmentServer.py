from fastapi import FastAPI
from pydantic import BaseModel
import threading

import json

app = FastAPI()

class Item(BaseModel):
    device_id : int
    Location1_x: int
    Location1_y: int
    Location2_x: int
    Location2_y: int

file_lock = threading.Lock()

def save_to_json(data):
    try:
        existing_data = []
        try:
            with open('./data.json', 'r') as existing_file:
                existing_data = json.load(existing_file)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        existing_data.append(data)
        with open('./data.json', 'w') as json_file:
            json.dump(existing_data, json_file, indent=2)
            json_file.write('\n')
    except Exception as e:
        print(f"Error saving to JSON: {e}")

@app.get("/")
def root():
    return {"hello this is assignmentServer!!!"}

@app.post("/request")
async def assignmentServer(item: Item):
    save_to_json(item.dict())
    return item

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)