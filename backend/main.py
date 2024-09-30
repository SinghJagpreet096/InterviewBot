from fastapi import FastAPI
from services.data_process import DataProcess


app = FastAPI()

@app.post("/process_data")
async def process_data(files):
    resume = files["resume"]
    job_description = files["job_description"]
    chat_history = DataProcess().process_data(resume, job_description)
    return {"message": "Data processed successfully"}

@app.get("/status")
async def status():
    return {"status": "Server is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
