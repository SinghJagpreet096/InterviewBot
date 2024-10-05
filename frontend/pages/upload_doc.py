import streamlit as st
from streamlit import session_state as ss
from utilities import go_to_page, preview_documents
from requests_toolbelt.multipart.encoder import MultipartEncoder
import requests

def app():  
    url = "http://127.0.0.1:8000"
    with st.expander("Upload Files"):
        job_description = st.file_uploader("Upload a job description", type=["pdf", "docx"], key='job_description')
        resume = st.file_uploader("Upload a resume", type=["pdf", "docx"], key='resume')
        preview_documents(resume, job_description)
    st.write(requests.get(url + "/status"))
    if st.button("Process Data"):
        if resume:
            try:
                resume = MultipartEncoder(fields={"file": ("resume", resume, "application/pdf")})
                job_description = MultipartEncoder(fields={"file": ("job_description", job_description, "application/pdf")})
                if requests.post(url + "/upload_file", data=resume, headers={"Content-Type": resume.content_type}, params={"filename":"resume"},timeout=8000).json() and \
                    requests.post(url + "/upload_file", data=job_description, headers={"Content-Type": job_description.content_type},params={"filename":"job_desc"}, timeout=8000).json():
                    st.write("Files uploaded successfully")
            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to the backend. Please ensure the server is running.")   

if __name__ == "__main__":      
    app()