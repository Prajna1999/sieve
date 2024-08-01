from sqlalchemy.orm import Session
# Sql alchemy models to interact with the db
from app.models.task import Task
# Pydantic models for type safety
from app.schemas.task import TaskCreate, TaskStatus


def create_task(db: Session, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_task(db: Session, task_id: int):
    return db.query(Task).filter(Task.id == task_id).first()


def get_tasks_by_job(db: Session, job_id: int, skip: int = 0, limit: int = 100):
    return db.query(Task).filter(Task.job_id == job_id).offset(skip).limit(limit).all()


def update_task_status(db: Session, task_id: int, status: TaskStatus):
    db_task = get_task(db, task_id)
    if db_task:
        db_task.status = status
        db.commit()
        db.refresh(db_task)
    return db_task
