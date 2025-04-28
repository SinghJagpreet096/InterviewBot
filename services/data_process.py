from services.app.embedding import Embeddings
from services.app.get_text import GetText
from services.app.chat_history import ChatHistory, ChatHistory_CPP
from typing import BinaryIO
import logging


class DataProcess:
    def __init__(self):
        self.getText = GetText()
        self.embedding = Embeddings()

    def process_data(self, document: BinaryIO | None) -> str:
        """
        Process the data from the uploaded files
        """
        logging.info("Processing files")
        text = self.getText.pdf(document)
        return text
    
    
    def create_context(self, session_id:str, resume_text:str, job_description_text:str) -> ChatHistory:
        """
        Create context for the chatbot
        """
        context = f"Job Description: {job_description_text}\n Resume: {resume_text}"
        self.embedding.create_embedding(text=context,session_id=session_id)
        retriever = self.embedding.load_retriever(session_id=session_id)
        ch = ChatHistory(session_id=session_id,retriever=retriever)
        return ch
    
# def main():
#     data_process = DataProcess()
#     ret = data_process.process_data("/Users/jagpreetsingh/ML_Projects/interviewbot/1724448810.pdf", "/Users/jagpreetsingh/ML_Projects/interviewbot/1724448810.pdf")
#     print("Data processed successfully",ret)


# if __name__ == "__main__":
#     main()

    