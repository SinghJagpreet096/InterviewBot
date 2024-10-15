import streamlit as st
from backend.app.config import Config
from backend.app.model import Model
from backend.app.get_text import GetText
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer
from backend.app.chat_history import ChatHistory
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
import av
from video import VideoRecorder
from backend.app.audio import AudioProcessor
from backend.app.speechToText import speech_to_text
from backend.utilities import display_message
from backend.app.embedding import Embeddings

# Initialize model and config

# cnf = Config()
# get_text = GetText()
SESSION_ID = "123"
# EMBED = Embeddings()

# st.title("Simple Chatbot App")

# record = st.button("Start Answering")

# # Upload Files
# with st.expander("Upload Files"):
#     job_description = st.file_uploader("Upload a job description", type=["pdf", "docx"], key='job_description')
#     resume = st.file_uploader("Upload a resume", type=["pdf", "docx"], key='resume')

# # Display uploaded files
# with st.sidebar:
#     if 'pdf_resume' not in ss:
#         ss.pdf_resume = None

#     if 'pdf_jd' not in ss:
#         ss.pdf_jd = None

#     # Assign uploaded files to session state
#     if resume:
#         ss.pdf_resume = resume

#     if job_description:
#         ss.pdf_jd = job_description
#     st.write("PDF Preview")
#     with st.expander("Click to view Resume", expanded=False):
#         if ss.pdf_resume and ss.pdf_resume.type == 'application/pdf':
#             binary_resume = ss.pdf_resume.getvalue()  # Get the binary content of the file
#             pdf_viewer(input=binary_resume, width=400, height=550)  # Display the PDF
#     with st.expander("Click to view Job Description", expanded=False):
#         # Display PDF preview for job description if it's a PDF
#         if ss.pdf_jd and ss.pdf_jd.type == 'application/pdf':
#             binary_jd = ss.pdf_jd.getvalue()  # Get the binary content of the file
#             pdf_viewer(input=binary_jd, width=400, height=550)  # Display the PDF

# # get text from uploaded files

# if job_description:
#     if job_description.type == 'application/pdf': 
#         job_description_text = get_text.pdf(job_description)
#         retriever = EMBED.get_embedding(text=job_description_text, chunk_size=10, chunk_overlap=2)
        
#     elif job_description.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
#         job_description_text = get_text.docx(job_description)
        
# if resume:
#     if resume.type == 'application/pdf':
#         resume_text = get_text.pdf(resume)
#     elif resume.type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
#         resume_text = get_text.docx(resume)

# # create prompt
# if job_description and resume:
#     prompt = cnf.promt(job_description=job_description_text, resume=resume_text)
#     # st.write(prompt)
# # Display questions
start_interview = st.button("Begin Interview")
end_interview = st.button("End Interview")
# write them in container
for _ in range(20):
    st.write("\n")
# st.write("Interview Questions will be displayed here")
col1, col2 = st.columns([4,1])

# Display questions

if 'conversation' not in st.session_state:
    st.session_state.conversation = []

# Function to add a new message to the conversation
def add_message(role, message):
    st.session_state.conversation.append({"sender":role,
                                          "message": message})

if start_interview:
    # Generate prompt and get questions
    model = Model(session_id=SESSION_ID)
    llm = model.llm
    ch = ChatHistory(session_id=SESSION_ID, llm=llm, retriever=retriever)
    rag_chain = ch.chain()  
    question = model.get_response(rag_chain=rag_chain,session_history=ch.get_session_history , query="")
    print(question)
    add_message("Interviewer", question.content)
with col1:
    response = st.text_input("", label_visibility="collapsed",placeholder="Type your response here")
with col2:
    submit = st.button("Submit")
# Get response
if submit:
    add_message("Candidate", response)
    question = model.get_response(rag_chain=rag_chain,session_history=ch.get_session_history , query=response)
    # st.write(questions)
    add_message("Interviewer", question.content)


# if record:
#     response = speech_to_text()
#     add_message("Candidate", response)
#     question = model.chain_response(response,CHAT_HISTORY)
#     # st.write(questions)
#     add_message("Interviewer", question.content)
# for chat in st.session_state.conversation:
#     display_message(message=chat['message'], sender=chat['sender'])
    
if end_interview:
    summary = model.get_response(rag_chain=rag_chain,session_history=ch.get_session_history , query="summarize the interview")
    st.write(f"Summary:{summary.content}")
    st.write("Interview Ended")
    st.session_state.conversation = []
    

