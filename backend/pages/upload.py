import streamlit as st
from streamlit import session_state as ss
from utilities import go_to_page, preview_documents
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests
from services.data_process import DataProcess
from pages import chat

def app():  
    with st.expander("Upload Files"):
        job_description = st.file_uploader("Upload a job description", type=["pdf", "docx"], key='job_description')
        resume = st.file_uploader("Upload a resume", type=["pdf", "docx"], key='resume')
        preview_documents(resume, job_description)
    submit = st.button("Process Data")
    if submit and resume and job_description:
        context = DataProcess().process_data(resume, job_description)
        st.write("Data processed successfully")
        chat.app(context)
        
if __name__ == "__main__":      
    app()