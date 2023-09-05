from fastapi import FastAPI, Depends, Path, HTTPException
from database import engineconn
from models import AssignmentTbl #, ScoreTbl, ScoreRequestQueueTbl, SubgroupDetailTbl, MotionCodeInfoTbl, AvailableEdgeDeviceTbl, SubgroupInfoTbl
from schemas import Sch_AssignmentTbl

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()
conn = engine.connection()

@app.get("/")
async def first_get():
    example = session.query(AssignmentTbl).all()
    return example

# main http
# @app.get("/", description="This is World Time CRUD API")
# def root():
#     return {"hello this is World Time CRUD API!!!"}

# @app.get("/read")
# def read():
#     query =  session.query(AssignmentTbl)
#     return query.all()

# @app.get('/read/{device_id}')
# def get_device_info(device_id: int):
#     query = session.query(AssignmentTbl).filter(AssignmentTbl.device_id == device_id)
#     return query.all()

# @app.post("/create")
# def create(new_subgroup_info: Item):
#     new_subgroup_info = AssignmentTbl(index = new_subgroup_info.index,
#                                   device_id= new_subgroup_info.device_id,
#                                   task_subgroup_code = new_subgroup_info.task_subgroup_code,
#                                   take_yn = new_subgroup_info.take_yn,
#                                   insrt_ts = new_subgroup_info.insrt_ts,
#                                   updt_ts = new_subgroup_info.updt_ts)
#     session.add(new_subgroup_info)
#     session.commit()
#     return

# @app.delete('/delete/{device_id}')
# def delete_device(device_id: int):
#     session.query(AssignmentTbl).filter(AssignmentTbl.device_id == device_id).delete()
#     return