from fastapi import FastAPI, HTTPException
# from config import db
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from starlette import status
# from route.city import cityPath
# python -m venv venv
app = FastAPI()



# app.include_router(cityPath)
@app.get('/get', status_code=status.HTTP_200_OK)
async def hello():
    return "Hello server is workingsssss"
