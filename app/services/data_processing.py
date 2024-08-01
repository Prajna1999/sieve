import csv
import PyPDF2
from sqlalchemy.orm import Session
from app.models.data_processing import DataProcessingJob, DataProcessingTask
from app.schemas.data_processing import DataProcessingJobCreate, DataProcessingTaskCreate


def create_data_processing_job(db: Session, job: DataProcessingJobCreate):
    db_job = DataProcessingJob(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def create_data_processing_task(db: Session, task: DataProcessingTaskCreate):
    db_task = DataProcessingTask(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def process_csv(file_path: str):
    result = []
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            result.append(row)
    return result


def process_pdf(file_path: str):
    result = []
    with open(file_path, 'rb') as pdffile:
        pdfreader = PyPDF2.PdfFileReader(pdffile)
        for page in range(pdfreader.numPages):
            result.append(pdfreader.getPage(page).extract_text())
    return result


def process_data(db: Session, job_id: int):
    job = db.query(DataProcessingJob).filter(
        DataProcessingJob.id == job_id).first()
    if not job:
        return None

    if job.file_type == "csv":
        result = process_csv(job.file_path)
    elif job.file_type == "pdf":
        result = process_pdf(job.file_path)
    else:
        return None

    task = DataProcessingTask(
        job_id=job.id, task_type=f"process_{job.file_type}", status="completed", result=str(result))
    db.add(task)
    job.status = "completed"
    db.commit()
    return job
