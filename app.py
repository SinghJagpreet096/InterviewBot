import streamlit as st
from config import Config
from model import Model
from get_text import GetText
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer

# Initialize model and config

cnf = Config()
get_text = GetText()

st.title("Simple Chatbot App")

# Upload Files
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
    elif job_description.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        job_description_text = get_text.docx(job_description)

if resume:
    if resume.type == 'application/pdf':
        resume_text = get_text.pdf(resume)
    elif resume.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        resume_text = get_text.docx(resume)

# create prompt
if job_description and resume:
    prompt = cnf.promt(job_description=job_description_text, resume=resume_text)
    model = Model(template=prompt)
# Generate prompt and get questions

start_interview = st.button("Begin Interview")
end_interview = st.button("End Interview")
# write them in container
for _ in range(20):
    st.write("\n")
# st.write("Interview Questions will be displayed here")
col1, col2 = st.columns([4,1])
with col1:
    response = st.text_input("", label_visibility="collapsed",placeholder="Type your response here")
with col2:
    submit = st.button("Submit")
# Display questions

if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Function to add a new message to the conversation
def add_message(role, message):
    st.session_state.conversation.append(f"{role}: {message}")

if start_interview:
    question = model.chain_response()
    add_message("Interviewer", question)

# Get response
if submit:
    add_message("Candidate", response)
    question = model.chain_response(response)
    # st.write(questions)
    add_message("Interviewer", question)
for message in st.session_state.conversation:
    st.write(message)

if end_interview:
    summary = model.chain_response(f"Summarize the interview")  
    st.write(f"Summary:{summary}")
    st.write("Interview Ended")
    st.session_state.conversation = []
    

