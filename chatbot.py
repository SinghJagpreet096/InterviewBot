import streamlit as st
from streamlit import session_state as ss
from model import Model
from utilities import display_message
from chat_history import ChatHistory
from embedding import Embeddings

SESSION_ID = "123"
embed = Embeddings()
def chat(job_description_text):
    
    start_interview = st.button("Begin Interview")
    end_interview = st.button("End Interview")
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

# Function to add a new message to the conversation
    def add_message(role, message):
        st.session_state.conversation.append({"sender":role,
                                            "message": message})
    retriever = embed.get_embedding(job_description_text)
    if start_interview:
        # Generate prompt and get questions
        model = Model(session_id=SESSION_ID)
        llm = model.llm
        ch = ChatHistory(session_id=SESSION_ID, llm=llm, retriever=retriever)
        rag_chain = ch.chain()  
        question = model.get_response(rag_chain=rag_chain,session_history=ch.get_session_history , query="What is Task Decomposition?")
        print(question)
        add_message(role="Interviewer", message=question)
    col1, col2 = st.columns([4,1])
    with col1:
        response = st.text_input("", label_visibility="collapsed",placeholder="Type your response here")
    with col2:
        submit = st.button("Submit")
    # Get response
    # if submit:
    #     add_message("Candidate", response)
    #     question = model.get_response(rag_chain=rag_chain,session_history=ch.get_session_history , query=response)
    #     # st.write(questions)
    #     add_message("Interviewer", question.content)


    # if record:
    #     response = speech_to_text()
    #     add_message("Candidate", response)
    #     question = model.chain_response(response,CHAT_HISTORY)
    #     # st.write(questions)
    #     add_message("Interviewer", question.content)
    # for chat in st.session_state.conversation:
    #     display_message(message=chat['message'], sender=chat['sender'])
        
    # if end_interview:
    #     summary = model.get_response(rag_chain=rag_chain,session_history=ch.get_session_history , query="summarize the interview")
    #     st.write(f"Summary:{summary.content}")
    #     st.write("Interview Ended")
    #     st.session_state.conversation = []
        
if __name__ == "__main__":
    job_description_text = """JAGPREET SINGH
+16479682319 | singhjagpreet4218@gmail.com | Toronto, ON, Canada | LinkedIn | GitHub | Portfolio
SKILLS
Programming and Libraries: Python, MySQL, PL/SQL, BigQueryML, Tensorflow, Pytorch, Hugging Face, Scikit-Learn, NumPy,
Pandas
Machine Learning: Natural Language Processing (NLP), Neural Network, Deep Learning, LLMs, Computer Vision, Transformers,
OpenAI, RAG, Generative AI, CNN, RNN, LSTM, Transformers
MLOps: Docker, CI/CD, Github actions, RAG, Kubernetes, MLFlow, Kubeflow, Model Deployment, Git, Linux scripting, Azure Data
Factory, Azure Databricks, Azure Machine Learning, AWS Sagemaker
Cloud and Databases: Oracle, MySql, BigQuery, Google Cloud Platform(GCP), MySQL, NoSQL, Hadoop
Data Visualization and Analysis: Power BI, Tableau, Matplotlib, Seaborn
EXPERIENCE
Cognizant Remote
Machine Learning Engineer January 2022 - December 2022
• Rectifying issues with training existing Machine learning models.
• Identified and developed components to extend functionality of the product by 50%.
• Rapid development of Multiple Image classification Models using Teachable Machine creating reject classes increasing
accuracy by 10%.
• Served as the sole Machine Learning Engineer, collaborating closely with a director to develop and deploy advanced ML
models on AWS and local servers.
Cognizant Remote
July 2020 - December 2021
Data Analyst • Transformed clinical trials data into analytical reports using PL/SQL in Oracle LSH.
• Contributed to over 100+ research studies, with a specialization in more than 15 Oncology trials, supporting research and
development in clinical trials.
• Reduced standard report delivery time from 10 to 6 days through workflow optimization.
• Executed end-to-end data processing, from extraction to loading into BI tools.
• Implemented an issue log system, streamlining the allocation of tickets to technical teams from 15 to 5 per week.
• Established a knowledge base, optimizing onboarding efficiency by reducing new employee training duration from 4 weeks
to 10 days.
PUBLICATIONS
Singh, J., et al. (2023). “Alzheimer's diagnostic with OASIS.” STEM Fellowship, leveraging open data analytics and machine learning
to improve the diagnosis of diseases, patients' care, and support: Proceedings from the 2023 Inter-University Big Data and AI Challenge,
5. URL: Alzheimer's diagnostic with OASIS
PROJECTS
Generative Pre-trained Transformer(GPT) | Python , PyTorch January 2024 - March 2024
• Developed a custom Small Language Model by training a GPT architecture from scratch, based on OpenAI's GPT-2
framework.
• Fine-tuned the model into a conversational Chatbot with capabilities as a casual Language Model.
• Implemented distributed training using accelerate from Hugging face.
• Link to project
Document Reader | Langchain, LLMs, GPT 3.5 November 2023 - December 2023
• Engineered Document Reader, an intuitive chatbot enabling swift inquiries with file uploads (text/PDF) of up to 20 MBs
• Developed the application using Chainlit and harnessed the power of OpenAI's gpt-3.5-turbo LLMs model for robust
implementation.
• Link to project
American Sign Language | Computer Vision, Mediapipe • The project showcases hand sign detection through the integration of TensorFlow Lite and Flask.
May 2023 - August 2023
• It involves capturing frames from a video stream using OpenCV, extracting posture coordinates with Media Pipe, and utilizing
these coordinates within a model to classify the detected hand signs.
• Link to project
Text To SQL | LLMs, Gemma, NLP, Hugging Face January 2024 - April 2024
• Fine-tuned Gemma-2b, a pre-trained transformer, to generate SQL queries from English instructions.
• Integrated the model with SQLite to utilize schema information, providing crucial context for enhanced query prediction.
• Link to project
EDUCATION
Lambton College Master's, Artificial Intelligence and Machine Learning January 2023 - August 2024
GPA: 3.49
Guru Nanak Dev University Bachelor's, Computer Science
June 2016 - May 2020"""
    chat(job_description_text)

