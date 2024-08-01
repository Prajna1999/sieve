from pydantic import BaseModel, Field
from typing import List,Optional
from datetime import datetime

class JobBase(BaseModel):
    title: str=Field(...,min_length=1, max_length=100)
    description:Optional[str]=Field(None,max_length=500)

class JobCreate(JobBase):
    pass

class JobInDB(JobBase):
    id:int
    created_at:datetime
    updated_at:datetime

    class Config:
        orm_mode=True

class Job(JobInDB):
    pass