import sys

from fastapi import FastAPI

version = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"

app = FastAPI()


@app.get("/")
async def read_root():
    message = f"Hello world! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}
