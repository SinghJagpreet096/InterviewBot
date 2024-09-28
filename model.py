from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import HumanMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chat_history import ChatHistory
from langchain_chroma import Chroma
from langchain_core.output_parsers import StrOutputParser
from embedding import Embeddings


class Model:
    # llm = ChatOllama(model="llama3.1")
    def __init__(self, session_id:str):
        self.llm = ChatOllama(model="llama3.1")
        self.session_id = session_id
        self.config = {"configurable": {"session_id": session_id}}
        self.promt = "What is your name?"
    
    def get_response(self, rag_chain, session_history, query:str):    
        conversational_rag_chain = RunnableWithMessageHistory(
        rag_chain,
        session_history,
        input_messages_key="input",
        history_messages_key="chat_history",
        output_messages_key="answer",
        )
        response = conversational_rag_chain.invoke(
        {"input": query},
        config={
            "configurable": {"session_id": self.session_id}
        },  # constructs a key "abc123" in `store`.
        )["answer"]
    
        return response



if __name__ == "__main__":
    embed = Embeddings()
    session_id = "123"
    retriever = embed.load_retriever()
    print(retriever)
    m = Model(session_id=session_id)
    llm = m.llm
    ch = ChatHistory(session_id=session_id, llm=llm, retriever=retriever)
    rag_chain = ch.chain()
    
    response = m.get_response(rag_chain=rag_chain,session_history=ch.get_session_history , query="What is Task Decomposition?")
    # print(response)


    
   