import streamlit as st
from streamlit import session_state as ss
import requests
from backend.utilities import display_message


def app():
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
        question = requests.get("http://localhost:8000/question",params={"answer":"begin interview"}).json()
        add_message("AI Assistant", question["question"])
        # for message, sender in ss.conversation:
        #     st.markdown(display_message(message, sender), unsafe_allow_html=True)
        # display_message(question["question"], "AI Assistant")
    col1, col2 = st.columns([4,1])
    
    with col1:
        answer = st.text_input("",placeholder="Type your response here")
    with col2:
        submit = st.button("Submit")
    # Get response
    if submit:
        add_message("Candidate", answer)
        # display_message(answer, "Candidate")
        question = requests.get("http://localhost:8000/question",params={"answer":answer}).json()
        # Call the backend to get the response
        add_message("AI Assistant", question["question"])
        # display_message(question["question"], "AI Assistant")
        
    if end_interview:
        st.write("Interview Ended")
        summary = requests.get("http://localhost:8000/question",params={"answer":"Sumarise the interview"}).json()
        add_message("AI Assistant", summary["question"])
        # display_message(summary["question"], "AI Assistant")
        st.session_state.conversation = []
    for m in ss.conversation:
        display_message(m["message"], m["sender"])

if __name__ == "__main__":
    app()
