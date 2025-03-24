from fastapi import FastAPI
app = FastAPI()

@app.get("/welcome")
def welcome():
    return {
        "message": "Welcome to FastAPI"
        }

@app.get("/welcome1")
def welcome():
    return {
        "message1": "Welcome to FastAPI 1"
        }