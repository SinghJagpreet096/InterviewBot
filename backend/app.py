import streamlit as st
from streamlit import session_state as ss
# 
cand, emp = st.columns(2)

with cand:
    candidate = st.button("Candidate")
    if candidate:
        
        # candidate_login = st.Page("candidate/login.py")
        # pg = st.navigation([candidate_login])
        if "session_id" not in ss:
            ss.session_id = "1234"
        st.switch_page("pages/candidate_login.py")
        
        
with emp:
    employer = st.button("Employer")
    if employer:
        pass 
