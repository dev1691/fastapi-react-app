# build a schema using pydantic
from pydantic import BaseModel

class users(BaseModel):
    Firstname:str
    Lastname:str
    email:str
    password_:str

    
    class Config:
        orm_mode = True