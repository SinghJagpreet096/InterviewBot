from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
import time
import os
import streamlit as st

# TODO
# 1. find a better model
def text_to_speech(text:str):
    '''
    Function to convert text to speech using Google Text-to-Speech (gTTS) API.
    The function saves the audio file as MP3 and then converts it to WAV format.
    The audio file is then played using simpleaudio package.

    Parameters:
    text (str): The text to be converted to speech.

    Returns:
    None
    '''
    
    # Convert the text to speech
    tts = gTTS(text=text, lang='en', speed=1.5)
    audio_data = BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    # Convert MP3 file to WAV format
    audio = AudioSegment.from_file(audio_data, format="mp3")
    play(audio) 
    return audio_data
if __name__ == "__main__":
    sen = "Hello, Welcome to the world of text to speech conversion using Python."
    # for word in sen.split():
    #     # yield word + " "
    #     text_to_speech(word)
    text_to_speech(sen)
    # st.audio(text_to_speech(sen), format='audio/mp3')
    
        
