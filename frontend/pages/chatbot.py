import streamlit as st
from streamlit import session_state as ss
import requests


def app():
    # buttons
    start_interview = st.button("Begin Interview")
    end_interview = st.button("End Interview")
    # Initialize the conversation
    if "conversation" not in st.session_state:
        st.session_state.conversation = []
    # Function to add a new message to the conversation
    def add_message(role, message):
        st.session_state.conversation.append({"sender":role,
                                            "message": message})
    if start_interview:
        st.write("Interview Started")
        question = requests.get("http://localhost:8000/question",params={"answer":"begin interview"}).json()
        add_message("AI Assistant", question["question"])
        display_message(question["question"], "AI Assistant")
    col1, col2 = st.columns([4,1])
    with col1:
        answer = st.text_input("", label_visibility="collapsed",placeholder="Type your response here")
    with col2:
        submit = st.button("Submit")
    # Get response
    if submit:
        add_message("Candidate", answer)
        display_message(answer, "Candidate")
        # Call the backend to get the response
        question = "Question from the model"
        add_message("AI Assistant", question)
        display_message(question, "AI Assistant")
        
    if end_interview:
        st.write("Interview Ended")
        st.session_state.conversation = []

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

if __name__ == "__main__":
    app()
