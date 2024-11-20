import streamlit as st
from services.prediction import get_prediction
from utilities import response_generator
from streamlit import session_state as ss
from services.app.speechToText import speech_to_text
from threading import Thread


start_interview = st.button("Start Interview")
record = st.button("Record")
answer = st.chat_input("Type your response here...")
session_id = ss.session_id

with st.container(border=True, ):
    if "conversation" not in st.session_state:
        st.session_state.conversation = []
    for message in st.session_state.conversation:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    if start_interview:
        print("Interview started")
        question = get_prediction(ss.context, session_id, "begin interview")
        # gtts.text_to_speech(question)
        # speech_thread(question)
        with st.chat_message("assistant"):
            response = st.write_stream(response_generator(question))
        st.session_state.conversation.append({"role": "assistant", "content": response})
        # st.session_state.conversation.append(question)
    if record:
        voice = speech_to_text()
        with st.chat_message("user"):
            st.markdown(voice)
        st.session_state.conversation.append({"role": "user", "content": voice})
        response = get_prediction(ss.context, session_id, voice)
        # gtts.text_to_speech(response)
        # speech_thread(response)
        with st.chat_message("assistant"):
            # text_to_speech(response)
            response = st.write_stream(response_generator(response))
        st.session_state.conversation.append({"role": "assistant", "content": response})
    if answer:
        with st.chat_message("user"):
            st.markdown(answer)
        st.session_state.conversation.append({"role": "user", "content": answer})
        response = get_prediction(ss.context, session_id, answer)
        # gtts.text_to_speech(response)
        # speech_thread(response)
        with st.chat_message("assistant"):
            # text_to_speech(response_generator(response))
            response = st.write_stream(response_generator(response))
        st.session_state.conversation.append({"role": "assistant", "content": response})

