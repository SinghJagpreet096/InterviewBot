import streamlit as st
from streamlit import session_state as ss
from upload_doc import upload_page
from chatbot import chat



# Set up session state for navigation
if 'page' not in ss:
    ss.page = 'upload'
# Main page after upload
# def main_page():
#     st.title("Main Page")
#     st.write("Documents successfully uploaded. You are now on the main page!")

# Render the correct page based on session state
if ss.page == 'upload':
    upload_page()
elif ss.page == 'chat':
    job_description_text = ss.job_description_text
    chat(job_description_text)



