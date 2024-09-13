from meta_ai_api import MetaAI
# from langchain.llms import metaai
import langchain
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain.chains import LLMChain


class Model:
    def __init__(self, template:str):
        self.meta_ai = MetaAI()
        self.prompt = ChatPromptTemplate.from_template(template)
        self.model = OllamaLLM(model="llama3.1")

    def get_response(self, query):
        response = self.meta_ai.prompt(
            message=query)
        return response['message']
    
    def chain_response(self, query=""):
        chain = self.prompt | self.model
        response = chain.invoke({"question": query})
        return response



if __name__ == "__main__":
    while True:
        model = Model(template=" you are an assistant")
        query = input("Enter your query: ")
        response = model.chain_response(query)
        print(response)
    