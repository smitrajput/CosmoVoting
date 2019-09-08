from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum
from services.enc_service import EncService


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "API working !! Hurrayy...!"}


@app.get("/key/generate/")
async def generate_key():

    response = EncService.generate_key()
    return response


@app.post("/encrypt/")
async def encrypt(request: dict):

    response = EncService.encrypt(request)
    return response


@app.post("/decrypt/")
async def decrypt(request: dict):

    response = EncService.decrypt(request)
    return response


