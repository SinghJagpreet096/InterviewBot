import streamlit as st
from streamlit import session_state as ss
# from pages import chat, upload
from utilities import go_to_page, preview_documents, display_message
from services.prediction import get_prediction
from services.data_process import DataProcess

session_id = "1234"
st.set_page_config(page_title="Resume Chatbot", page_icon=":robot:")
with st.expander("Upload Files"):
    job_description = st.file_uploader("Upload a job description", type=["pdf", "docx"], key='job_description')
    resume = st.file_uploader("Upload a resume", type=["pdf", "docx"], key='resume')
    preview_documents(resume, job_description)
    process_files = st.button("Process Data")
start_interview = st.button("Start Interview")
end_interview = st.button("End Interview")
col1, col2 = st.columns([4,1])
with col1:
    answer = st.text_input("",placeholder="Type your response here")
with col2:
    submit = st.button("Submit")
if process_files:
    context = DataProcess().process_data(job_description, resume)
    ss.context = context
    st.write("Data processed successfully")
    print("Data processed successfully",ss.context)

if 'conversation' not in st.session_state:
    ss.conversation = []

if start_interview:
    st.session_state.conversation = []
    st.session_state.conversation.append("Interview started")
    st.write("Interview started")
    print("Interview started")
    question = get_prediction(ss.context, session_id, "begin interview")
    st.session_state.conversation.append(question)
    st.write(question)

if submit:
    st.session_state.conversation.append(answer)
    question = get_prediction(ss.context, session_id, answer)
    st.session_state.conversation.append(question)
    st.write(question)

if end_interview:
    st.session_state.conversation = []
    st.write("Interview ended")
    print("Interview ended")
    summary = get_prediction(ss.context, session_id, "summarize the interview")
    st.session_state.conversation.append(summary)
    st.write(summary)




    
