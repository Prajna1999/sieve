from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.job import Job, JobCreate
from app.services import job_service

router = APIRouter()


@router.post("/", response_model=Job)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    return job_service.create_job(db, job)


@router.get("/{job_id}", response_model=Job)
def read_job(job_id: int, db: Session = Depends(get_db)):
    db_job = job_service.get_job(db, job_id)
    if db_job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return db_job


@router.get("/", response_model=List[Job])
def read_jobs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    jobs = job_service.get_jobs(db, skip=skip, limit=limit)
    return jobs
