class Config:
    def promt(self, job_description:str, resume:str):
        PROMT = f"""Job Description:{job_description} 
        Resume: {resume} 
        You are an Interviewer. 
        Based on given job description and resume of the candidate ask questions
        Ask only questions and do not provide any explanation or answer to the question."""
        return PROMT