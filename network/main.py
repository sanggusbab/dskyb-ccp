from fastapi import FastAPI, Depends, Path, HTTPException
from database import engineconn
from models import AssignmentTbl, MotionCodeInfoTbl #, ScoreTbl, ScoreRequestQueueTbl, SubgroupDetailTbl, MotionCodeInfoTbl, AvailableEdgeDeviceTbl, SubgroupInfoTbl
from schemas import Sch_AssignmentTbl
from pydantic import BaseModel
from starlette.responses import JSONResponse

app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()
conn = engine.connection()

# main http
@app.get("/", description="This is World Time CRUD API")
def root():
    return {"hello this is World Time CRUD API!!!"}