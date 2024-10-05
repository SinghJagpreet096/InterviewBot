from fastapi import FastAPI, File, Form, Path, UploadFile, Response
from services.data_process import DataProcess
import logging
from typing import TextIO, BinaryIO, Annotated
from pydantic import BaseModel
import io
from services.prediction import get_prediction
import os


app = FastAPI()
 
logging.basicConfig(level=logging.DEBUG)
# class PDFData(BaseModel):
#      file: UploadFile
# resume: BinaryIO | None = None
# job_description: BinaryIO | None = None

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR,exist_ok=True)


@app.post("/upload_file")
async def upload_file(filename: str,file: bytes = File(...)): 
    """
    Upload a file to the server
    """
    try:
        path = f"{UPLOAD_DIR}/{filename}.pdf"
        file = io.BytesIO(file)
        # Saving the file
        with open(path, "wb") as f:
            f.write(file.read())
        return True
    except Exception as e:
        logging.error(e)
        return False
    
@app.get("/question")
async def generate_question(answer: str | None = None):
    """
    Generate a question based on the answer provided
    """
    try:
        resume = "uploads/resume.pdf"
        job_description = "uploads/job_description.pdf"
        dp = DataProcess()
        ch = dp.process_data(resume, job_description)
        question = get_prediction(chat_history=ch, session_id="abc123", query=answer)
        print(question)
        return {"question": question}
        # return {"question": "Question from the model"}
    except Exception as e:
        logging.error(e)
        return {"question": "Error generating question"}
    


@app.get("/status")
async def status():
    return {"status": "Server is running"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)