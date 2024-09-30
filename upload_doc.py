import streamlit as st
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer
from get_text import GetText
from embedding import Embeddings
from chatbot import chat
from utilities import go_to_page
# from index import go_to_main


get_text = GetText()
EMBED = Embeddings()
# Upload page
# Function to switch pages


def upload_page():  
    st.title("Upload Documents")
    with st.expander("Upload Files"):
        job_description = st.file_uploader("Upload a job description", type=["pdf", "docx"], key='job_description')
        resume = st.file_uploader("Upload a resume", type=["pdf", "docx"], key='resume')

# Display uploaded files
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

    # get text from uploaded files

    if job_description:
        if job_description.type == 'application/pdf': 
            job_description_text = get_text.pdf(job_description)
            print(type(job_description_text))
            st.session_state['job_description_text'] = job_description_text
            
        elif job_description.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
            job_description_text = get_text.docx(job_description)
            
    # if resume:
    #     if resume.type == 'application/pdf':
    #         resume_text = get_text.pdf(resume)
    #     elif resume.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
    #         resume_text = get_text.docx(resume)

    
    
    if st.button('Upload and Continue'):
        # st.write("Documents successfully uploaded. You are now on the main page!")
        
        go_to_page("chat")
        
if __name__ == "__main__":
    upload_page()
