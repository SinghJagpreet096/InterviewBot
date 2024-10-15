import streamlit as st
from streamlit import session_state as ss
from pages import chat, upload

begin = st.button("Begin INTERVIEW")
if begin:
    context = upload.app()







