class Config:
    def promt(self, job_description:str, resume:str):
        PROMT = f"""Job Description:{job_description} 
        Resume: {resume} 
        You are an Interviewer. 
        Based on given job description and resume of the candidate ask question to the candidate, one question at a time.
        Ask only question and do not provide any explanation or answer to the question."""
        return PROMT