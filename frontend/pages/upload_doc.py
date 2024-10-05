import streamlit as st
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer
import requests
from typing import BinaryIO
from requests_toolbelt.multipart.encoder import MultipartEncoder


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
                response = requests.post(url + "/upload_file", data=resume, headers={"Content-Type": resume.content_type}, timeout=8000).json()   
                st.write(response)
            except requests.exceptions.ConnectionError:
                st.error("Cannot connect to the backend. Please ensure the server is running.")   

def preview_documents(resume, job_description):
    with st.sidebar:
        if 'pdf_resume' not in ss:
            ss.pdf_resume = None

        if 'pdf_jd' not in ss:
            ss.pdf_jd = None

        # Assign uploaded files to session state
        if resume:
            ss.pdf_resume = resume

        if job_description:
            ss.pdf_jd = job_description
        st.write("PDF Preview")
        with st.expander("Click to view Resume", expanded=False):
            if ss.pdf_resume and ss.pdf_resume.type == 'application/pdf':
                binary_resume = ss.pdf_resume.getvalue()  # Get the binary content of the file
                pdf_viewer(input=binary_resume, width=400, height=550)  # Display the PDF
        with st.expander("Click to view Job Description", expanded=False):
            # Display PDF preview for job description if it's a PDF
            if ss.pdf_jd and ss.pdf_jd.type == 'application/pdf':
                binary_jd = ss.pdf_jd.getvalue()  # Get the binary content of the file
                pdf_viewer(input=binary_jd, width=400, height=550)  # Display the PDF

if __name__ == "__main__":      
    app()