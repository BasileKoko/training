import uvicorn
from fastapi import FastAPI

from config import APP_HOST, APP_PORT, LOG_LEVEL
from google import genai
from dotenv import load_dotenv

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run("main:app", host=APP_HOST, port=APP_PORT,reload=LOG_LEVEL)



@app.get("/")
async def root():
    load_dotenv()

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents="Explain how AI works in a few words",
    )

    print(response.text)






