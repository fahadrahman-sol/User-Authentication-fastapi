# main.py
from fastapi import FastAPI
from database import engine, Base
from routes import users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router, prefix="/users")

@app.get("/")
def root():
    return {"message": "Welcome to the Authentication API"}
