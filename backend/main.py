from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
import uuid

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "../uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.get("/")
def read_root():
    return {"message": "Backend Running"}

@app.post("/upload")
async def upload_file(
    department: str = Form(...),
    document_type: str = Form(...),
    file: UploadFile = File(...)
):
    unique_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{unique_id}_{file.filename}")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {
        "status": "success",
        "file_saved": file_path,
        "department": department,
        "document_type": document_type
    }