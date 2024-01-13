from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Item(BaseModel):
    request_id: int

def save_to_json(data):
    try:
        existing_data = []
        try:
            with open('../D_public/data.json', 'r') as existing_file:
                existing_data = json.load(existing_file)
                existing_data.append(data)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        with open('../D_public/data.json', 'w') as json_file:
            json.dump(existing_data, json_file, indent=2)
            json_file.write('\n')
    except Exception as e:
        print(f"Error saving to JSON: {e}")


@app.get("/")
def root():
    return {"hello this is D1_server!!!"}

@app.post("/request")
async def D1_server(item: Item):
    save_to_json(item.request_id)
    return item
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)