from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.data_processing import DataProcessingJob, DataProcessingJobCreate, DataProcessingTask, DataProcessingTaskCreate
from app.services import data_processing

router = APIRouter()


@router.post("/jobs/", response_model=DataProcessingJob)
def create_job(job: DataProcessingJobCreate, db: Session = Depends(get_db)):
    return data_processing.create_data_processing_job(db, job)


@router.get("/jobs/{job_id}", response_model=DataProcessingJob)
def read_job(job_id: int, db: Session = Depends(get_db)):
    job = db.query(DataProcessingJob).filter(
        DataProcessingJob.id == job_id).first()
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


@router.post("/tasks/", response_model=DataProcessingTask)
def create_task(task: DataProcessingTaskCreate, db: Session = Depends(get_db)):
    return data_processing.create_data_processing_task(db, task)


@router.get("/tasks/{task_id}", response_model=DataProcessingTask)
def read_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(DataProcessingTask).filter(
        DataProcessingTask.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@router.post("/jobs/{job_id}/process", response_model=DataProcessingJob)
def process_job(job_id: int, db: Session = Depends(get_db)):
    result = data_processing.process_data(db, job_id)
    if result is None:
        raise HTTPException(
            status_code=404, detail="Job not found or processing failed")
    return result
