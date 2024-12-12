import streamlit as st
from utilities import preview_documents
from services.data_process import DataProcess
from streamlit import session_state as ss
# from services.session_state import SessionState


# Set page configuration
st.set_page_config(page_title="Upload Page", page_icon="📤" )

def main(session_id):
    with st.expander("Upload Files"):
        job_description = st.file_uploader("Upload a job description", type=["pdf", "docx"], key='job_description',label_visibility='hidden')
        resume = st.file_uploader("Upload a resume", type=["pdf", "docx"], key='resume')
        preview_documents(resume, job_description)
        
        process_files = st.button("Process Data")

    if  process_files:
        if job_description is None or resume is None:
            st.error("Please upload both files")
            return
        try:
            context = DataProcess().process_data(session_id, job_description, resume)
            st.success("Data processed successfully")
            if "context" not in ss:
                ss.context = context
            st.switch_page("pages/video.py")
        except Exception as e:
            st.error("Oops! Something went wrong")
            raise e
    left, right = st.columns([1, 1])
    with left:
        prev = st.button("Previous")
        if prev:
            st.switch_page("pages/candidate_login.py")
    with right:
        next = st.button("Next")
        if next:
            st.switch_page("pages/video.py")
       

if __name__ == "__main__":
    session_id = ss.session_id
    main(session_id)