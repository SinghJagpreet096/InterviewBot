from services import data_process
from services import prediction
import click
import sys
from llama_cpp import Llama

if sys.argv[1] == "data_process":
    data_process.main()
elif sys.argv[1] == "prediction":   
    prediction.main()

# if __name__ == "__main__":
    

#     llm = Llama.from_pretrained(
#         repo_id="singhjagpreet/Llama-3.2-1B-Instruct-Q8_0-GGUF",
#         filename="llama-3.2-1b-instruct-q8_0.gguf",
#         verbose=False
#     )

#     res = llm.create_chat_completion(
#         messages = [
#             {
#                 "role": "user",
#                 "content": "What is the capital of France?"
#             }
#         ]
#     )

    # print("response:",res)
