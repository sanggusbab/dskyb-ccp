from fastapi import FastAPI
from pydantic import BaseModel
import threading
file_lock = threading.Lock()
import json

app = FastAPI()

class Item(BaseModel):
    assignment_id: int

file_lock = threading.Lock()

def append_to_file(data):
    with open("../G_public/data.json", "r") as json_file:
        json_data = json.load(json_file)
    json_data['data'].append(data)
    print(json_data)
    with open("../G_public/data.json", "w") as file:
        json.dump(json_data, file, default=str)

@app.get("/")
def root():
    return {"hello this is G1_server!!!"}


@app.post("/")
async def G1_server(item: Item):
    with file_lock:
        append_to_file(item.assignment_id)
    return item


def G1_run():
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)

if __name__ == "__main__":
    G1_run()