from fastapi import APIRouter
from services.data_process import DataProcess
from services.app.model import Model


def get_prediction(chat_history, session_id, query):
    m = Model(session_id=session_id, llm=chat_history.llm)
    response = m.get_response(rag_chain=chat_history.chain(), session_history=chat_history.get_session_history, query=query)
    # print(response)
    return response

def main():
    resume = "/Users/jagpreetsingh/ML_Projects/interviewbot/1724448810.pdf"
    job_description = "/Users/jagpreetsingh/ML_Projects/interviewbot/sample-job-description.pdf"
    session_id = "abc123"
    ch = DataProcess().process_data(session_id, resume, job_description)
    
    while True:
        query = input("Enter your query: ")
        get_prediction(ch,session_id,query)
    
if __name__ == "__main__":
    main()