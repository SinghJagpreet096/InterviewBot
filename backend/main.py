from fastapi import FastAPI, File, Form, Path, UploadFile, Response
from services.data_process import DataProcess
import logging
from typing import TextIO, BinaryIO, Annotated
from pydantic import BaseModel
import io
from services.prediction import get_prediction

app = FastAPI()
 
logging.basicConfig(level=logging.DEBUG)
# class PDFData(BaseModel):
#      file: UploadFile
resume: BinaryIO | None = None
job_description: BinaryIO | None = None

@app.post("/upload_file")
async def upload_file(file: bytes = File(...)): 
    """
    Upload a file to the server
    """
    try:
        resume = io.BytesIO(file)
        job_description = io.BytesIO(file) 
    except Exception as e:
        logging.error(e)
        return {"message": "Error processing the file"}
    return {"message": "File uploaded successfully"}
    

@app.get("/question")
async def generate_question(answer: str | None = None):
    """
    Generate a question based on the answer provided
    """
    ch = DataProcess().process_data(resume, job_description)
    question = get_prediction(ch, answer, "abc123")
    return {"question": question}


@app.get("/status")
async def status():
    return {"status": "Server is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)