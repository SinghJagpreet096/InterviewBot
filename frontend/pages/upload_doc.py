import streamlit as st
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer
import requests

def app():  
    st.title("Upload Documents")
    job_description = st.file_uploader("Upload a job description", type=["pdf", "docx"], key='job_description')
    resume = st.file_uploader("Upload a resume", type=["pdf", "docx"], key='resume')
    preview_documents(resume, job_description)
    if st.button("Process Data"):
        # Send the uploaded files to the backend for processing
        files = {"resume": resume, "job_description": job_description}
        try:
            response = requests.post("http://127.0.0.1:8000/process_data", files=files)
            st.write(response.json())
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
