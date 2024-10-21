import streamlit as st
from streamlit import session_state as ss


# Dictionary to map page names to page modules
# PAGES = {
#     "Page 1": "pages.upload_doc",
#     "Page 2": "pages.chatbot",
# }

# Create a sidebar for navigation
# st.sidebar.title("Navigation")
# selection = st.sidebar.radio("Go to", list(PAGES.keys()))

# # Load the page module based on the selection
# page = __import__(PAGES[selection])
# page.app() 
if __name__=="__main__":
    if 'conversation' not in st.session_state:
        ss.conversation = []
    st.title("Chat Interface with Aligned Messages")

