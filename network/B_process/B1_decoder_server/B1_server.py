from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()

def save_to_json(data):
    try:
        existing_data = []
        try:
            with open('../B_public/data.json', 'r') as existing_file:
                existing_data = json.load(existing_file)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        existing_data.append(data)
        with open('../B_public/data.json', 'w') as json_file:
            json.dump(existing_data, json_file, indent=2)
            json_file.write('\n')
    except Exception as e:
        print(f"Error saving to JSON: {e}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    Location1_x: str
    Location1_y: str
    Location2_x: str
    Location2_y: str
    currentTime: str
    userId: str
    text: str

@app.get("/")
def root():
    return {'hello this is B1_server!!!'}

@app.post("/request")
async def B1_server(item: Item):
    data = {
        'Location1_x': item.Location1_x,
        'Location1_y': item.Location1_y,
        'Location2_x': item.Location2_x,
        'Location2_y': item.Location2_y,
        'currentTime': item.currentTime,
        'userId': item.userId,
        'text': item.text
    }
    print(data)
    save_to_json(data)
    return {'response': data['text']}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)