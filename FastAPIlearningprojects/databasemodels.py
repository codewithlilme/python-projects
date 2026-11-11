from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Lesson(Base):

    __tablename__ = "Lessons"
    id = Column(Integer,index=True,primary_key=True) 
    name = Column(String)
    Lecturer = Column(String)
    fees = Column(Float)