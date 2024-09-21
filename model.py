from langchain_ollama import ChatOllama
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.messages import HumanMessage
from chat_history import ChatHistory


class Model:
    def __init__(self, system_message:str, session_id:str):
        self.model = ChatOllama(model="llama3.1")
        self.session_id = session_id
        self.config = {"configurable": {"session_id": session_id}}
        # self.chain = LLMChain() 
    def get_response(self, query):
        response = self.meta_ai.prompt(
            message=query)
        return response['message']
    
    def chain_response(self, content, chat_history):    
        with_message_history = RunnableWithMessageHistory(self.model, chat_history.get_session_history)
        response = with_message_history.invoke([HumanMessage(content=content)],
        config=self.config,
    )
        return response



if __name__ == "__main__":
    session_id = "abc2"
    CHAT_HISTORY = ChatHistory(session_id)
    model = Model(system_message="you are an assitant",session_id=session_id)
    query = "my name is john"
    res = model.chain_response(query,chat_history=CHAT_HISTORY)
    print(res.content)
    query = "what is my name"
    res = model.chain_response(query,chat_history=CHAT_HISTORY)
    print(res.content)
   