import streamlit as st
from streamlit import session_state as ss


def app():
    start_interview = st.button("Begin Interview")
    end_interview = st.button("End Interview")
    if 'conversation' not in st.session_state:
        st.session_state.conversation = []
# Function to add a new message to the conversation
    def add_message(role, message):
        st.session_state.conversation.append({"sender":role,
                                            "message": message})
    if start_interview:
        st.write("Interview Started")
    col1, col2 = st.columns([4,1])
    with col1:
        response = st.text_input("", label_visibility="collapsed",placeholder="Type your response here")
    with col2:
        submit = st.button("Submit")
    # Get response
    if submit:
        add_message("Candidate", response)
        
    if end_interview:
        st.write("Interview Ended")
        st.session_state.conversation = []
        
if __name__ == "__main__":
    app()
