from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from chromadb.config import Settings
import chromadb
from langchain_core.vectorstores import VectorStoreRetriever


class Embeddings:
    def __init__(self, chunk_size=1000, chunk_overlap=200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    def get_embedding(self, text: str, session_id: str):
        splits = self.text_splitter.split_text(text)
        persist_directory = f"./{session_id}/chroma_db"
        vectorstore = Chroma.from_texts(texts=splits,
                                        embedding=OllamaEmbeddings(model="nomic-embed-text"),
                                        persist_directory=persist_directory,
                                        #  client_settings=chroma_settings
                                         )
       
        retriever = vectorstore.as_retriever()
        return retriever
    
    def load_retriever(self, persist_directory="./chroma_db"):
        # Load the Chroma vector store from disk
        vectorstore = Chroma(persist_directory=persist_directory,
            # client_settings=chroma_settings
        ) 
        # Get the retriever from the loaded vector store
        retriever = vectorstore.as_retriever()
        return retriever


# if __name__ == "__main__":
#     text = """JAGPREET SINGH
# +16479682319 | singhjagpreet4218@gmail.com | Toronto, ON, Canada | LinkedIn | GitHub | Portfolio
# SKILLS
# Programming and Libraries: Python, MySQL, PL/SQL, BigQueryML, Tensorflow, Pytorch, Hugging Face, Scikit-Learn, NumPy,
# Pandas
# Machine Learning: Natural Language Processing (NLP), Neural Network, Deep Learning, LLMs, Computer Vision, Transformers,
# OpenAI, RAG, Generative AI, CNN, RNN, LSTM, Transformers
# MLOps: Docker, CI/CD, Github actions, RAG, Kubernetes, MLFlow, Kubeflow, Model Deployment, Git, Linux scripting, Azure Data
# Factory, Azure Databricks, Azure Machine Learning, AWS Sagemaker
# Cloud and Databases: Oracle, MySql, BigQuery, Google Cloud Platform(GCP), MySQL, NoSQL, Hadoop
# Data Visualization and Analysis: Power BI, Tableau, Matplotlib, Seaborn
# EXPERIENCE
# Cognizant Remote
# Machine Learning Engineer January 2022 - December 2022
# • Rectifying issues with training existing Machine learning models.
# • Identified and developed components to extend functionality of the product by 50%.
# • Rapid development of Multiple Image classification Models using Teachable Machine creating reject classes increasing
# accuracy by 10%.
# • Served as the sole Machine Learning Engineer, collaborating closely with a director to develop and deploy advanced ML
# models on AWS and local servers.
# Cognizant Remote
# July 2020 - December 2021
# Data Analyst • Transformed clinical trials data into analytical reports using PL/SQL in Oracle LSH.
# • Contributed to over 100+ research studies, with a specialization in more than 15 Oncology trials, supporting research and
# development in clinical trials.
# • Reduced standard report delivery time from 10 to 6 days through workflow optimization.
# • Executed end-to-end data processing, from extraction to loading into BI tools.
# • Implemented an issue log system, streamlining the allocation of tickets to technical teams from 15 to 5 per week.
# • Established a knowledge base, optimizing onboarding efficiency by reducing new employee training duration from 4 weeks
# to 10 days.
# PUBLICATIONS
# Singh, J., et al. (2023). “Alzheimer's diagnostic with OASIS.” STEM Fellowship, leveraging open data analytics and machine learning
# to improve the diagnosis of diseases, patients' care, and support: Proceedings from the 2023 Inter-University Big Data and AI Challenge,
# 5. URL: Alzheimer's diagnostic with OASIS
# PROJECTS
# Generative Pre-trained Transformer(GPT) | Python , PyTorch January 2024 - March 2024
# • Developed a custom Small Language Model by training a GPT architecture from scratch, based on OpenAI's GPT-2
# framework.
# • Fine-tuned the model into a conversational Chatbot with capabilities as a casual Language Model.
# • Implemented distributed training using accelerate from Hugging face.
# • Link to project
# Document Reader | Langchain, LLMs, GPT 3.5 November 2023 - December 2023
# • Engineered Document Reader, an intuitive chatbot enabling swift inquiries with file uploads (text/PDF) of up to 20 MBs
# • Developed the application using Chainlit and harnessed the power of OpenAI's gpt-3.5-turbo LLMs model for robust
# implementation.
# • Link to project
# American Sign Language | Computer Vision, Mediapipe • The project showcases hand sign detection through the integration of TensorFlow Lite and Flask.
# May 2023 - August 2023
# • It involves capturing frames from a video stream using OpenCV, extracting posture coordinates with Media Pipe, and utilizing
# these coordinates within a model to classify the detected hand signs.
# • Link to project
# Text To SQL | LLMs, Gemma, NLP, Hugging Face January 2024 - April 2024
# • Fine-tuned Gemma-2b, a pre-trained transformer, to generate SQL queries from English instructions.
# • Integrated the model with SQLite to utilize schema information, providing crucial context for enhanced query prediction.
# • Link to project
# EDUCATION
# Lambton College Master's, Artificial Intelligence and Machine Learning January 2023 - August 2024
# GPA: 3.49
# Guru Nanak Dev University Bachelor's, Computer Science
# June 2016 - May 2020"""
#     print(type(text))
#     embed = Embeddings()
#     ret = embed.get_embedding(text=text)
#     print(ret)
#     l = embed.load_retriever()
#     print(l)
#     # retriever = embed.load_retriever()
#     # print(retriever)

    
    