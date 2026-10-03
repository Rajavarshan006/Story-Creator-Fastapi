from sqlalchemy import Column, Integer, String, DateTime,Boolean, ForeignKey, JSON
from sqlalchemy.orm import func
from sqlalchemy.orm import relationship


from db.database import Base

class story(Base):
     
    __tablename__ = "Stories"

    id = Column(Integer, primary_key = True, index = True)

    title = Column(String, index = True)

    content = Column(String, index = True)

    session_id = Column(String, index = True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    nodes = relationship("StoryNode", back_populates="story") ##one to many relationship with StoryNode


class StoryNode(Base):
    __tablename__ = "StoryNodes"

    id = Column(Integer, primary_key=True, index=True)
    story_id = Column(Integer, ForeignKey("Stories.id"), index = True)

    content = Column(String, index=True)
    is_root = Column(Boolean, default=False)

    is_ending = Column(Boolean, default=False)
    is_winning_ending = Column(Boolean, default=False)
    options = Column(JSON, default=[])  ##list of options for the next node

    story = relationship("story", back_populates="nodes")  ##many to one relationship with story