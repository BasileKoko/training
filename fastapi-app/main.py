import uvicorn
from fastapi import FastAPI

from config import APP_HOST, APP_PORT, LOG_LEVEL


app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host=APP_HOST, port=APP_PORT,reload=LOG_LEVEL)



@app.get("/")
async def root():
    return {"message": "Hello World"}