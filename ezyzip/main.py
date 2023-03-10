import uvicorn
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from schema import users as Schemausers
from schema import users
from models import users as Modelusers

import os
from dotenv import load_dotenv

load_dotenv('.env')


app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get("/register")
async def users():
    users = db.session.query(Modelusers(Firstname=users.Firstname,Lastname=users.Lastname,email=users.email,password_=users.password_))
    return users

@app.post('/register', response_model=Schemausers)
async def users(users: Schemausers):
    db_users = Modelusers(Firstname=users.Firstname,Lastname=users.Lastname,email=users.email,password_=users.password_)
    db.session.add(db_users)
    db.session.commit()
    return db_users

@app.get("/home")
async def users():
    users = db.session.query(Modelusers(email=users.email,password_=users.password_))
    return users


# @app.get('/users/')
# async def users():
#     users = db.session.query(Modelusers(email=users.email,password_=users.password_))
#     return users

if __name__ == '__main__':
    uvicorn.run(app, port=8000)