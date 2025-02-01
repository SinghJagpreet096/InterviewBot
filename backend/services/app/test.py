import streamlit as st
from streamlit_webrtc import webrtc_streamer 
from streamlit import session_state as ss

# from services.app.speechToText import moonshineASR
from live_captions import LiveCaptions  
import streamlit as st
import argparse
import os                                                                           
import time
from queue import Queue
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
asr_engine = LiveCaptions("moonshine/base")

if "recording" not in ss:
    ss.recording = False
   
record = st.button("Start Interview")
stop = st.button("Stop")

class StopLiveCaptions(Exception):
    pass

def live_cap(record, stop):
    if record:
        ss.recording = True
        with st.container(border=True, height=200 ):
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

            global caption_cache 
            caption_cache = []
            lookback_size = LOOKBACK_CHUNKS * CHUNK_SIZE
            speech = np.empty(0, dtype=np.float32)
            recording = False
            print("Press 'Stop' button to quit live captions.\n")
            with stream:
                # asr_engine.print_captions("Ready...", caption_cache)
                try:
                    while True:
                        if stop:
                            raise StopLiveCaptions
                            
                        chunk, status = q.get()
                        if status:
                            print(status)
                            

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
                                text = asr_engine.end_recording(speech)
                                caption_cache.append(text)

                        elif recording:
                            # Possible speech truncation can cause hallucination.

                            if (len(speech) / asr_engine.SAMPLING_RATE) > MAX_SPEECH_SECS:
                                recording = False
                                text = asr_engine.end_recording(speech, caption_cache)
                                asr_engine.soft_reset(vad_iterator)

                            if (time.time() - start_time) > MIN_REFRESH_SECS:
                                # asr_engine.print_captions(asr_engine.transcribe(speech), caption_cache)
                                start_time = time.time()
                                
                except StopLiveCaptions:
                    stream.close()
                    print("Stopping live captions.")

                    if recording:
                        while not q.empty():
                            chunk, _ = q.get()
                            speech = np.concatenate((speech, chunk))
                        text = asr_engine.end_recording(speech, do_print=False)
                        caption_cache.append(text)
                    if caption_cache:
                        print(f"Cached captions.\n{' '.join(caption_cache)}") 
                    return caption_cache
                    # return caption_cache


if __name__ == "__main__":
    output = live_cap(record, stop)
    if output:
        print(" ".join(output))