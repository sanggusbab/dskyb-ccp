from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Item(BaseModel):
    device_id: int
    task_subgroup_code: int

def is_duplicate(data, existing_data):
    for existing_item in existing_data:
        if existing_item.get("task_subgroup_code") == data.get("task_subgroup_code"):
            return True
    return False

def save_to_json(data):
    try:
        existing_data = []
        try:
            with open('../F_public/data.json', 'r') as existing_file:
                existing_data = json.load(existing_file)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        # Convert Item instance to dictionary
        data_dict = data.dict()

        # Check for duplicate task_subgroup_code
        if is_duplicate(data_dict, existing_data):
            return False

        existing_data.append(data_dict)
        with open('../F_public/data.json', 'w') as json_file:
            json.dump(existing_data, json_file, indent=2)
            json_file.write('\n')
        
        return True
    except Exception as e:
        print(f"Error saving to JSON: {e}")
        return False

@app.get("/")
def root():
    return {"hello this is F1_server!!!"}

@app.post("/request")
async def F1_server(item: Item):
    if save_to_json(item):
        return item
    else:
        return False


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8004)