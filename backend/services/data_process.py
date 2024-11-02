from services.app.embedding import Embeddings
from services.app.get_text import GetText
from services.app.chat_history import ChatHistory
from typing import BinaryIO


class DataProcess:
    def __init__(self):
        self.getText = GetText()
        self.embedding = Embeddings()

    def process_data(self, session_id:str, resume: BinaryIO | None = None, job_description: BinaryIO | None = None) -> ChatHistory:
        resume_text = self.getText.pdf(resume)
        job_description_text = self.getText.pdf(job_description)
        context = f"Job Description: {job_description_text}\n Resume: {resume_text}"
        self.embedding.create_embedding(text=context,session_id=session_id)
        retriever = self.embedding.load_retriever(session_id=session_id)
        ch = ChatHistory(session_id=session_id, retriever=retriever)
        return ch
def main():
    data_process = DataProcess()
    ret = data_process.process_data("/Users/jagpreetsingh/ML_Projects/interviewbot/1724448810.pdf", "/Users/jagpreetsingh/ML_Projects/interviewbot/1724448810.pdf")
    print("Data processed successfully",ret)


if __name__ == "__main__":
    main()

    