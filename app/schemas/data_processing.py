from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from enum import Enum


class FileType(str, Enum):
    CSV = "csv"
    PDF = "pdf"


class DataProcessingJobCreate(BaseModel):
    file_type: FileType
    file_path: str


class DataProcessingJobUpdate(BaseModel):
    status: str


class DataProcessingTaskCreate(BaseModel):
    job_id: int
    task_type: str


class DataProcessingTaskUpdate(BaseModel):
    status: str
    result: Optional[str] = None


class DataProcessingTask(BaseModel):
    id: int
    job_id: int
    task_type: str
    status: str
    result: Optional[str]
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class DataProcessingJob(BaseModel):
    id: int
    file_type: FileType
    file_path: str
    status: str
    created_at: datetime
    updated_at: datetime
    tasks: List[DataProcessingTask]

    class Config:
        orm_mode = True
