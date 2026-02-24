from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Student Document Automation Backend Running"}
