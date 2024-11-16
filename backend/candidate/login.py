import streamlit as st

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
        st.write("Welcome, **{}**!".format(username))
    else:
        st.error("Invalid username or password.")
