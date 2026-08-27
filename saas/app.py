from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def instant():
    return "Welcome to the SAAS Application! Live Deployment from production!"