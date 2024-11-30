from fastapi import FastAPI

app = FastAPI()

@app.get("/") # Request
def ola():
    return {"Olá":"Mundo"}