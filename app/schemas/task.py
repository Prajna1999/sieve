from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime
from enum import Enum

class TaskStatus(str,Enum):
    PENDING="pending"
    RUNNING="running"
    COMPLETED="completed"
    FAILED="failed"

class TaskBase(BaseModel):
    job_id:int
    name:str=Field(..., min_length=1,max_length=100)
    status:TaskStatus=TaskStatus.PENDING

class TaskCreate(TaskBase):
    pass
class TaskInDB(TaskBase):
    id:int
    created_at:datetime
    updated_at:datetime

    class Config:
        orm_mode=True

class Task(TaskInDB):
    pass