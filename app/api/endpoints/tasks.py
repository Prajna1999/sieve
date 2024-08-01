from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.db.session import get_db
from app.schemas.task import Task, TaskCreate, TaskStatus
from app.services import task_service

router = APIRouter()


@router.post("/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return task_service.create_task(db, task)


@router.get("/{task_id}", response_model=Task)
def read_task(task_id: int, db: Session = Depends(get_db)):
    db_task = task_service.get_task(db, task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task


@router.get("/job/{job_id}", response_model=List[Task])
def read_tasks_by_job(job_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    tasks = task_service.get_tasks_by_job(db, job_id, skip=skip, limit=limit)
    return tasks


@router.put("/{task_id}/status", response_model=Task)
def update_task_status(task_id: int, status: TaskStatus, db: Session = Depends(get_db)):
    db_task = task_service.update_task_status(db, task_id, status)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return db_task
