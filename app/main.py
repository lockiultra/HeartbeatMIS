from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db import create_tables
from app.routers.patients import patients_router
from app.routers.doctors import doctors_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print('Tables is ready')
    yield


app = FastAPI(lifespan=lifespan)

@app.get('/')
async def main():
    return {"Status": "OK"}

app.include_router(patients_router, prefix='/patients')
app.include_router(doctors_router, prefix='/doctors')
