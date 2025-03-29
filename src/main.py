from fastapi import FastAPI # type: ignore
from dotenv import load_dotenv # type: ignore
load_dotenv('.env') # Load environment variables from .env file
from routes import base, data

app = FastAPI()

app.include_router(base.base_router)
app.include_router(data.data_router)
