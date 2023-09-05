from typing import List, Optional
from pydantic import BaseModel

class Sch_AssignmentTbl(BaseModel):
    index : int
    device_id : int
    task_subgroup_code : int
    take_yn : str
    insrt_ts : str
    updt_ts : str