import streamlit as st
from streamlit import session_state as ss
# from pages import chat, upload
from utilities import go_to_page, preview_documents, response_generator
from services.prediction import get_prediction
from services.data_process import DataProcess
from services.app.speechToText import speech_to_text
from services.app.textToSpeech import text_to_speech
import shutil
import cv2

st.set_page_config(page_title="Resume Chatbot", page_icon=":robot:")
session_id = "1234"
## TODO: add a session id generator

main, chat = st.columns([3,2])
with main:  
    with st.container():
    # add_message("AI Assistant", "Hello! I am your AI Assistant. I will be conducting your interview today.")
        with st.expander("Upload Files"):
            job_description = st.file_uploader("Upload a job description", type=["pdf", "docx"], key='job_description',label_visibility='hidden')
            resume = st.file_uploader("Upload a resume", type=["pdf", "docx"], key='resume')
            preview_documents(resume, job_description)
            
            process_files = st.button("Process Data")

        if process_files:
            context = DataProcess().process_data(session_id, job_description, resume)
            ss.context = context
            st.write("Data processed successfully")
            print("Data processed successfully",ss.context)
        # microphone = st.button("Start Interview")
        # video_capture = cv2.VideoCapture(1)
        start_interview = st.button("Start Interview")
        record = st.button("Record")
answer = st.chat_input("Type your response here...")

with chat:
    with st.container(border=True):
        if "conversation" not in st.session_state:
            st.session_state.conversation = []
        for message in st.session_state.conversation:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        if start_interview:
            print("Interview started")
            question = get_prediction(ss.context, session_id, "begin interview")
            text_to_speech(question)
            with st.chat_message("assistant"):
                response = st.write_stream(response_generator(question))
            st.session_state.conversation.append({"role": "assistant", "content": response})
            # st.session_state.conversation.append(question)
        if record:
            voice = speech_to_text()
            with st.chat_message("user"):
                st.markdown(voice)
            st.session_state.conversation.append({"role": "user", "content": voice})
            response = get_prediction(ss.context, session_id, voice)
            text_to_speech(response)
            with st.chat_message("assistant"):
                # text_to_speech(response)
                response = st.write_stream(response_generator(response))
            st.session_state.conversation.append({"role": "assistant", "content": response})
        if answer:
            with st.chat_message("user"):
                st.markdown(answer)
            st.session_state.conversation.append({"role": "user", "content": answer})
            response = get_prediction(ss.context, session_id, answer)
            text_to_speech(response)
            with st.chat_message("assistant"):
                # text_to_speech(response_generator(response))
                response = st.write_stream(response_generator(response))
            st.session_state.conversation.append({"role": "assistant", "content": response})

      
       

    
    




    
