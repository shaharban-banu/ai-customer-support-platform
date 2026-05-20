from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from app.routes.ticket_routes import (router)
from app.database.database import engine
from app.database.models import Base

Base.metadata.create_all(bind=engine)

app=FastAPI(title="Customer Support AI")

Instrumentator().instrument(app).expose(app)

app.include_router(router)

@app.get('/')
def home():
    return {'message':"Customer suppotr AI running....."}
