from fastapi import FastAPI, Depends, Path, HTTPException
from database import engineconn
from models import AssignmentTbl, MotionCodeInfoTbl #, ScoreTbl, ScoreRequestQueueTbl, SubgroupDetailTbl, MotionCodeInfoTbl, AvailableEdgeDeviceTbl, SubgroupInfoTbl
from schemas import Sch_AssignmentTbl#, Sch_RouteTbl
from pydantic import BaseModel
from starlette.responses import JSONResponse


app = FastAPI()

engine = engineconn()
session = engine.sessionmaker()
conn = engine.connection()


class Sch_RouteTbl(BaseModel):
    mode : int 

# main http
@app.get("/", description="This is World Time CRUD API")
def root():
    return {"hello this is World Time CRUD API!!!"}

@app.post("/rou", response_model=Sch_RouteTbl)
async def router(item: Sch_RouteTbl):
    if(item.mode == 1):
        end_user_client_process()
    elif(item.mode == 2):
        decoder_server_process()
    elif(item.mode == 3):
        request_client_process()
    elif(item.mode == 4):
        request_server_process()
    elif(item.mode == 5):
        score_request_client_process()
    elif(item.mode == 6):
        score_request_server_process()
    elif(item.mode == 7):
        scoring_server_process
    elif(item.mode == 8):
        scoring_client_process
    elif(item.mode == 9):
        assignment_client_process()
    elif(item.mode == 10):
        assignment_server_process()
    elif(item.mode == 11):
        report_client_process()
    elif(item.mode == 12):
        report_server_process()
    elif(item.mode == 13):
        allocation_client_process()
    elif(item.mode == 14):
        allocation_server_process()
    elif(item.mode == 15):
        parameter_control_client_process()
    else:
        print("error mode")
    return item

def end_user_client_process():
    print("end_user_client_process")
    decoder_server_process()
    return

def decoder_server_process():
    print("decoder_server_process")
    request_client_process()
    return

def request_client_process():
    print("request_client_process")
    request_server_process()
    return

def request_server_process():
    print("request_server_process")
    score_request_client_process()
    return

def score_request_client_process():
    print("score_request_client_process")
    score_request_server_process()
    return

def score_request_server_process():
    print("score_request_client_process")
    scoring_server_process()
    return

def scoring_server_process():
    print("scoring_server_process")
    scoring_client_process()
    return

def scoring_client_process():
    print("scoring_client_process")
    assignment_client_process()
    return

def assignment_client_process():
    print("assignment_server_process")
    assignment_server_process()
    return

def assignment_server_process():
    print("assignment_server_process")
    report_server_process()
    return

def report_server_process():
    print("report_server_process")
    report_client_process()
    return

def report_client_process():
    print("report_client_process")
    allocation_client_process()
    return

def allocation_client_process():
    print("allocation_client_process")
    allocation_server_process()
    return

def allocation_server_process():
    print("allocation_server_process")
    parameter_control_client_process()
    return

def parameter_control_client_process():
    print("parameter_control_client_process")
    return