import streamlit as st
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer

# Function to display user and AI messages with different alignments
def display_message(message, sender="Candidate"):
    if sender == "Candidate":
        # Right-aligned for User
        st.markdown(f"""
            <div style="
                text-align: right;
                border: 0.5px faded #e0e0e0; 
                border-radius: 10px; 
                padding: 10px; 
                margin-bottom: 10px; 
                background-color: #1a1616; 
                width: fit-content;
                margin-left: auto;">
                {message}<br>
            </div>
        """, unsafe_allow_html=True)
    else:
        # Left-aligned for AI Assistant
        st.markdown(f"""
            <div style="
                text-align: left;
                border: 0.5px faded #e0e0e0; 
                border-radius: 10px; 
                padding: 10px; 
                margin-bottom: 10px; 
                background-color: #1a1616; 
                width: fit-content;
                margin-right: auto;">
                <strong>{message}</strong><br>    
            </div>
        """, unsafe_allow_html=True)


def go_to_page(page:str):
    st.session_state.page = page

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

if __name__=="__main__":
# Streamlit app interface
    st.title("Chat Interface with Aligned Messages")

    # Example messages for user and AI assistant
    display_message("Hello! How can I assist you today?", "AI Assistant")
    display_message("I need help with a project.", "Candidate")
    display_message("Sure! What kind of project are you working on?", "AI Assistant")
    display_message("I am working on a chatbot project.", "Candidate")
