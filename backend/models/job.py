from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import func

from backend.db.database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key = true, index = True)
    job_id = Column(String, index = True)
    session_id = Column(Integer, index = True)
    theme = Column(String, index = True)
    status = Column(String, index = True)
    story_id = Column(Integer, index = True)
    error = Column(String, index = True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)