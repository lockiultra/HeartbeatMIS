from fastapi import FastAPI
from contextlib import asynccontextmanager
from db import create_tables
from routers.patients import patients_router


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
