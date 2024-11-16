import streamlit as st
from streamlit import session_state as ss
import requests
from utilities import display_message
from services.prediction import get_prediction

session_id = "1234"
def app(context):
    # buttons
    start_interview = st.button("Begin Interview")
    end_interview = st.button("End Interview")
    if 'conversation' not in st.session_state:
        ss.conversation = []
    # Function to add a new message to the conversation
    def add_message(role, message):
        ss.conversation.append({"sender":role,
                                            "message": message})
    if start_interview:
        st.write("Interview Started")

        question = get_prediction(context,session_id, "begin interview")
        add_message("AI Assistant", question["question"])
    col1, col2 = st.columns([4,1])
    with col1:
        answer = st.text_input("",placeholder="Type your response here")
    with col2:
        submit = st.button("Submit")
    # Get response
    if submit:
        add_message("Candidate", answer)
        # display_message(answer, "Candidate")
        question = get_prediction(context,session_id, answer)
        # Call the backend to get the response
        add_message("AI Assistant", question["question"])
        # display_message(question["question"], "AI Assistant")
        
    if end_interview:
        st.write("Interview Ended")
        summary = get_prediction(context,session_id, "summarize the interview")
        add_message("AI Assistant", summary["question"])
        # display_message(summary["question"], "AI Assistant")
        st.session_state.conversation = []
    for m in ss.conversation:
        display_message(m["message"], m["sender"])

if __name__ == "__main__":
    app()
