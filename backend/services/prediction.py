from fastapi import APIRouter
from services.data_process import DataProcess
from services.app.model import Model
import time
import logging
from llama_cpp import Llama

logger = logging.getLogger(__name__)


def get_prediction(chat_history, session_id, query):
    logging.info("loading model")
    m = Model(session_id=session_id, llm=chat_history.llm)
    response = m.get_response(rag_chain=chat_history.chain(), session_history=chat_history.get_session_history, query=query)
    # print(response)
    logging.info("prediction generated")
    return response

def main():
    resume = "/Users/jagpreetsingh/ML_Projects/interviewbot/1724448810.pdf"
    job_description = "/Users/jagpreetsingh/ML_Projects/interviewbot/sample-job-description.pdf"
    session_id = "abc124"
    ch = DataProcess().process_data(session_id, resume, job_description)
    
    while True:
        query = input("Enter your query: ")
        start = time.time()
        res = get_prediction(ch,session_id,query)
        end = time.time()
        print(f"Time taken: {end-start}")
        print(res)

# def main():
#     from llama_cpp import Llama

#     llm = Llama.from_pretrained(
#         repo_id="singhjagpreet/Llama-3.2-1B-Instruct-Q8_0-GGUF",
#         filename="llama-3.2-1b-instruct-q8_0.gguf",
#         verbose=False,
#     )
#     # while True:
#     # query = input("Enter your query: ")
#     start = time.time()
#     res = llm.create_chat_completion(
#         messages = [
#             {
#                 "role": "user",
#                 "content": "capital of india"
#             }
#         ],
#         response_format={
#         "type": "string",
#     },
#     temperature=0.7,
#     )
#     end = time.time()
#     print(f"Time taken: {end-start}")
#     print(res)
#     print(res["choices"][0]["message"]["content"])
    
if __name__ == "__main__":
    # main()
    pass
    