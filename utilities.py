import streamlit as st

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
if __name__=="__main__":
# Streamlit app interface
    st.title("Chat Interface with Aligned Messages")

    # Example messages for user and AI assistant
    display_message("Hello! How can I assist you today?", "AI Assistant")
    display_message("I need help with a project.", "User")
    display_message("Sure! What kind of project are you working on?", "AI Assistant")
