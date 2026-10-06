


# why do we need to create a separate table for jobs in the database?
#     LLM doesnot returns the story in one go
#     it returns the story in chunks so we need to keep track of job status.

# frontend -> submits jobs
# backend -> view the job

# frontend -> ask if job is done?
# backend -> reports the status of the job
# if job is done, frontend -> backend -> fetch the story from the database and display it to the user

from sqlalchemy import Column, Integer, String, DateTime, func

from backend.db.database import Base

class StoryJob(Base):
    __tablename__ = "story_jobs"

    id = Column(Integer, primary_key = true, index = True)
    job_id = Column(String, index = True,unique=True)
    session_id = Column(Integer, index = True)
    theme = Column(String, index = True)
    status = Column(String, index = True)
    story_id = Column(Integer, index = True)
    error = Column(String, index = True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    completed_at = Column(DateTime(timezone=True), nullable=True)

    