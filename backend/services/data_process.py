from services.app.embedding import Embeddings
from services.app.get_text import GetText
from services.app.chat_history import ChatHistory


class DataProcess:
    def __init__(self):
        self.getText = GetText()
        self.embedding = Embeddings()

    def process_data(self, resume, job_description):
        resume_text = self.getText.pdf(resume)
        job_description_text = self.getText.pdf(job_description)
        context = f"Job Description: {job_description_text}\n Resume: {resume_text}"
        retriever = self.embedding.get_embedding(text=context, chunk_size=200, chunk_overlap=10)
        ch = ChatHistory(session_id="abc123", retriever=retriever)

        return ch
    
if __name__ == "__main__":
    data_process = DataProcess()
    ret = data_process.process_data("/Users/jagpreetsingh/ML_Projects/interviewbot/1724448810.pdf", "/Users/jagpreetsingh/ML_Projects/interviewbot/1724448810.pdf")
    print("Data processed successfully",ret)