import streamlit as st

if "candidate" not in st.session_state:
    st.session_state.candidate = False

st.set_page_config(page_title="InterView B0T", page_icon=":robot_face:")

cand, emp = st.columns([1, 1])

st.write("select User type")
with cand:
    candidate = st.button("Candidate Login")
    login = st.Page("candidate/login.py", title="Login Page", icon=":material/add_circle:")
    upload = st.Page("candidate/upload.py", title="Upload Documents", )

with emp:
    employer = st.button("Employer Login")
    login = st.Page("employer/login.py", title="Login Page", icon=":material/add_circle:")

if candidate:
    st.session_state.candidate = True


if st.session_state.candidate:
    pg = st.navigation(
        {
            "candidate":[login, upload]
        }
        )
else:
    pg = st.navigation(
        {
            "employer":[login]
        }
        )

pg.run()