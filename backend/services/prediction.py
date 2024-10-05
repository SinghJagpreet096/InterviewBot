from fastapi import APIRouter
from services.data_process import DataProcess
from services.app.model import Model


def get_prediction(chat_history, session_id, query):
    m = Model(session_id=session_id, llm=chat_history.llm)
    response = m.get_response(rag_chain=chat_history.chain(), session_history=chat_history.get_session_history, query=query)
    print(response)
    return response

def main():
    resume = "/Users/jagpreetsingh/ML_Projects/interviewbot/1724448810.pdf"
    job_description = "/Users/jagpreetsingh/ML_Projects/interviewbot/1724448810.pdf"
    ch = DataProcess().process_data(resume, job_description)
    session_id = "abc123"
    get_prediction(ch, "What is your experience with Machine Learning?",session_id)

if __name__ == "__main__":
    main()