import streamlit as st
from streamlit_webrtc import webrtc_streamer
from services.prediction import get_prediction
from utilities import response_generator
from streamlit import session_state as ss
from services.app.speechToText import speechRecognitionASR
# from services.app.speechToText import moonshineASR
from services.app.live_captions import LiveCaptions  
import streamlit as st
import argparse
import os
import time
from queue import Queue
import keyboard
from pynput import keyboard

import numpy as np
from silero_vad import VADIterator, load_silero_vad
from sounddevice import InputStream

from moonshine_onnx import MoonshineOnnxModel, load_tokenizer   

CHUNK_SIZE = 512  # Silero VAD requirement with sampling rate 16000.
LOOKBACK_CHUNKS = 5
MAX_LINE_LENGTH = 80

# These affect live caption updating - adjust for your platform speed and model.
MAX_SPEECH_SECS = 15
MIN_REFRESH_SECS = 0.2

st.set_page_config(page_title="Video Page", page_icon="📹")
video = st.camera_input("You are Live Now")
session_id = ss.session_id
asr_engine = LiveCaptions("moonshine/base")

if "conversation" not in st.session_state:
        st.session_state.conversation = []

if "recording" not in st.session_state:
    st.session_state.recording = False

if "transcribed_text" not in st.session_state:
    st.session_state.transcribed_text = ""

left, mid,_mid, right = st.columns([1, 1, 1, 1])  
with left:
    start_interview = st.button("Start Interview")
    
with mid:
    record = st.button("Record")

with _mid:
      stop = st.button("Stop", )
    
with right:
       end = st.button("End Interview")

if start_interview:
        print("Interview started")
        question = get_prediction(ss.context, session_id, "begin interview")
        response = st.write_stream(response_generator(question))
        st.session_state.conversation.append({"role": "assistant", "content": response})

if record:
        vad_model = load_silero_vad(onnx=True)
        vad_iterator = VADIterator(
        model=vad_model,
        sampling_rate=asr_engine.SAMPLING_RATE,
        threshold=0.5,
        min_silence_duration_ms=300,
    )
        q = Queue()
        stream = InputStream(
        samplerate=asr_engine.SAMPLING_RATE,
        channels=1,
        blocksize=CHUNK_SIZE,
        dtype=np.float32,
        callback=asr_engine.create_input_callback(q),
    )   
    
        stream.start()

        caption_cache = []
        lookback_size = LOOKBACK_CHUNKS * CHUNK_SIZE
        speech = np.empty(0, dtype=np.float32)
        recording = False
        print("Press Ctrl+C to quit live captions.\n")
        with stream:
            asr_engine.print_captions("Ready...", caption_cache)
            try:
                while True:
                    if not st.session_state.recording:
                        raise KeyboardInterrupt
                    chunk, status = q.get()
                    if status:
                        print(status)
                        # st.write_stream(status)
                        st.write_stream(asr_engine.response_generator(status))
                        st.session_state.transcribed_text += status

                    speech = np.concatenate((speech, chunk))
                    if not recording:
                        speech = speech[-lookback_size:]

                    speech_dict = vad_iterator(chunk)
                    if speech_dict:
                        if "start" in speech_dict and not recording:
                            recording = True
                            start_time = time.time()

                        if "end" in speech_dict and recording:
                            recording = False
                            asr_engine.end_recording(speech, caption_cache)

                    elif recording:
                        # Possible speech truncation can cause hallucination.

                        if (len(speech) / asr_engine.SAMPLING_RATE) > MAX_SPEECH_SECS:
                            recording = False
                            asr_engine.end_recording(speech, caption_cache)
                            asr_engine.soft_reset(vad_iterator)

                        if (time.time() - start_time) > MIN_REFRESH_SECS:
                            asr_engine.print_captions(asr_engine.transcribe(speech), caption_cache)
                            start_time = time.time()
                            
            except KeyboardInterrupt: 
                stream.close()

                if recording:
                    while not q.empty():
                        chunk, _ = q.get()
                        speech = np.concatenate((speech, chunk))
                    asr_engine.end_recording(speech, do_print=False)
                if caption_cache:
                    print(f"Cached captions.\n{' '.join(caption_cache)}")   
                      

if end:
    
    response = get_prediction(ss.context, session_id, "summarise the conversation")
    
    st.write_stream(response_generator(response))
    st.balloons()
    st.session_state.conversation = []