from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class StoryJobBase(BaseModel):
        theme : str

class StoryJobResponse(BaseModel):
   job_id : str
   story_id : int
   status : str
   created_at : datetime
   completed_at : Optional[datetime] = None
   error : Optional[str] = None

   class Config:
        from attribute = True


class StoryJobCreate(StoryJobBase):
        pass


from typing import Optional
from pydantic import BaseModel
from datetime import datetime


class StoryJobBase(BaseModel):
        theme : str

class StoryJobResponse(BaseModel):
   job_id : str
   story_id : int
   status : str
   created_at : datetime
   completed_at : Optional[datetime] = None
   error : Optional[str] = None

   class Config:
        from attribute = True


class StoryJobCreate(StoryJobBase):
        pass