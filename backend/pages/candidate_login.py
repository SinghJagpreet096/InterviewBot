import streamlit as st
from streamlit import session_state as ss
import time

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
        if "session_id" not in ss:
            ss.session_id = f"{username}123"
        time.sleep(1)
        st.switch_page("pages/upload.py")
    else:
        st.error("Invalid username or password.")
