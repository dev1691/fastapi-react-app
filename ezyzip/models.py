from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base  = declarative_base()

class users(Base):
    __tablename__ = 'users'
    Firstname = Column(String , primary_key=True, index=True)
    Lastname = Column(String)
    email = Column(String)
    password_ = Column(String)
   
   





