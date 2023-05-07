from fastapi import FastAPI

app = FastAPI()

@app.get("/app")
def root():
    return {"message": "Hello RPi!"}

@app.get("/test")
def root():
    return {"message": "Test123"}
