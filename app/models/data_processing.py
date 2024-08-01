from sqlalchemy import Column, Integer, String, DateTime, Enum, ForeignKey, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.database import Base
from app.schemas.task import TaskStatus
from enum import Enum as PyEnum


class FileType(str, PyEnum):
    CSV = "csv"
    PDF = "pdf"


class DataProcessingJob(Base):
    __tablename__ = "data_processing_jobs"

    id = Column(Integer, primary_key=True, index=True)
    file_type = Column(Enum(FileType), nullable=True)
    file_path = Column(String(255), nullable=False)
    status = Column(Enum(TaskStatus), default=TaskStatus.PENDING)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    tasks = relationship("DataProcessingTask", back_populates="job")


class DataProcessingTask(Base):
    __tablename__ = "data_processing_tasks"

    id = Column(Integer, primary_key=True, index=True)
    job_id = Column(Integer, ForeignKey(
        "data_processing_jobs.id"), nullable=False)
    task_type = Column(String(50), nullable=False)
    status = Column(Enum(TaskStatus), default="pending")
    result = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    job = relationship("DataProcessingJob", back_populates="tasks")
