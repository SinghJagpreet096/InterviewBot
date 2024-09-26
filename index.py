from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from get_text import GetText
from langchain_chroma import Chroma
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough



llm = ChatOllama(model="llama3.1")
# write a long text here

docs = """
write a long text here
write a long text here
write a long text here
write a long text here
write a long text here
write a long text here
write a long text here

"""
embeddings = OllamaEmbeddings(model="nomic-embed-text",)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=10, chunk_overlap=2)
splits = text_splitter.split_text(docs)
vectorstore = Chroma.from_texts(splits, embeddings)
# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
