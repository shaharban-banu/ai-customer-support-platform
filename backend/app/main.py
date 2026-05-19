from fastapi import FastAPI
from app.routes.ticket_routes import (router)
from app.database.database import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)

app=FastAPI(title="Customer Support AI")

app.include_router(router)

@app.get('/')
def home():
    return {'message':"Customer suppotr AI running....."}
