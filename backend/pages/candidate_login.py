import streamlit as st
from streamlit import session_state as ss

# Set page configuration
# st.set_page_config(page_title="Login Page", page_icon="🔑")

# Predefined user credentials (for demonstration purposes)
USERNAME = "user"
PASSWORD = "pass123"

# Streamlit application layout
st.title("Login Page")

# Create input fields for login
username = st.text_input("Username")
password = st.text_input("Password", type="password")

# Login button
if st.button("Login"):
    if username == USERNAME and password == PASSWORD:
        st.success("Login successful!")
        session_id = ss.session_id
        st.switch_page("pages/upload.py")
    else:
        st.error("Invalid username or password.")
