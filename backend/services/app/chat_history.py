from langchain_core.chat_history import (
    BaseChatMessageHistory,
    InMemoryChatMessageHistory,
)
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
# from embedding import Embeddings
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_ollama import ChatOllama
from langchain_community.chat_message_histories import ChatMessageHistory

class ChatHistory:
    def __init__(self, session_id, retriever):
        self.history = {}
        self.session_id = session_id
        self.retriever = retriever
        self.llm = ChatOllama(model="llama3.1")

    def context(self):
        ### Contextualize question ###
        contextualize_q_system_prompt = """Given a chat history and the latest user question \
        which might reference context in the chat history, formulate a standalone question \
        which can be understood without the chat history. Do NOT answer the question, \
        just reformulate it if needed and otherwise return it as is."""
        contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        history_aware_retriever = create_history_aware_retriever(
            self.llm, self.retriever, contextualize_q_prompt
        )
        return history_aware_retriever
    
    def chain(self):
        ### Answer question ###
        ### Answer question ###
        history_aware_retriever = self.context()
        qa_system_prompt = """You are an assistant for question-answering tasks. \
        Use the following pieces of retrieved context to answer the question. \
        If you don't know the answer, just say that you don't know. \
        Use three sentences maximum and keep the answer concise.\

        {context}"""
        qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", qa_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        question_answer_chain = create_stuff_documents_chain(self.llm, qa_prompt)

        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)
        return rag_chain
    
    def get_session_history(self) -> BaseChatMessageHistory:
        if self.session_id not in self.history:
            self.history[self.session_id] = ChatMessageHistory()
        return self.history[self.session_id]
    
if __name__ == "__main__":
    text = """Sample text
    sample text
    sample text
    sample text"""
    
    retriever= Embeddings().get_embedding(text, chunk_size=10, chunk_overlap=2)
    
    ch = ChatHistory(session_id="abc123", retriever=retriever)
    rag_chain = ch.chain()  
    get_session_history = ch.get_session_history
    conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer",
)

    res = conversational_rag_chain.invoke(
        {"input": "What is Task Decomposition?"},
        config={
            "configurable": {"session_id": "abc123"}
        },  # constructs a key "abc123" in `store`.
    )["answer"]
    print(res)
    