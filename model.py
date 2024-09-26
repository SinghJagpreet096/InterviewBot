from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chat_history import ChatHistory
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
class Model:
    def __init__(self, system_message:str, session_id:str):
        self.system_message = system_message
        self.model = ChatOllama(model="llama3.1")
        self.session_id = session_id
        self.config = {"configurable": {"session_id": session_id}}
        self.promt = "What is your name?"
        
    def get_embedding(self, text, chunk_size=1000, chunk_overlap=200):
        embeddings = OllamaEmbeddings(model="nomic-embed-text",)
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=10, chunk_overlap=2)
        splits = text_splitter.split_text(text)
        vectorstore = Chroma.from_texts(splits, embeddings)
        retriever = vectorstore.as_retriever()
        return retriever
    
    def chain_response(self, content, chat_history):    
        with_message_history = RunnableWithMessageHistory(self.model, chat_history.get_session_history)
        response = with_message_history.invoke([HumanMessage(content=content)],
        config=self.config,
    )
        return response



if __name__ == "__main__":

    # model = Model(
    session_id = "abc2"
    CHAT_HISTORY = ChatHistory(session_id)
    model = Model(system_message="you are an assitant",session_id=session_id)
    # query = "my name is john"
    # res = model.chain_response(query,chat_history=CHAT_HISTORY)
    # print(res.content)
    # query = "what is my name"
    # res = model.chain_response(query,chat_history=CHAT_HISTORY)
    # print(res.content)

    ## get embedding
    print(model.get_embedding(text="hello world", chunk_size=2, chunk_overlap=1))
   