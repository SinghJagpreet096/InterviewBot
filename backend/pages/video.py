import streamlit as st
from streamlit_webrtc import webrtc_streamer
from services.prediction import get_prediction
from utilities import response_generator
from streamlit import session_state as ss
from services.app.speechToText import moonshineASR

st.set_page_config(page_title="Video Page", page_icon="📹")
video = st.camera_input("You are Live Now")
session_id = ss.session_id
asr_engine = moonshineASR()

if "conversation" not in st.session_state:
        st.session_state.conversation = []

left, mid, right = st.columns([1, 1, 1])  
with left:
    start_interview = st.button("Start Interview")
    
with mid:
    record = st.button("Record")
    
with right:
       end = st.button("End Interview")

if start_interview:
        print("Interview started")
        question = get_prediction(ss.context, session_id, "begin interview")
        response = st.write_stream(response_generator(question))
        st.session_state.conversation.append({"role": "assistant", "content": response})

if record:
        voice = asr_engine.speech_to_text()
        st.markdown(voice[0])
        st.session_state.conversation.append({"role": "user", "content": voice})
        response = get_prediction(ss.context, session_id, voice)
        response = st.write_stream(response_generator(response))
        st.session_state.conversation.append({"role": "assistant", "content": response})
if end:
    response = get_prediction(ss.context, session_id, "summarise the conversation")
    
    st.write_stream(response_generator(response))
    st.balloons()
    st.session_state.conversation = []