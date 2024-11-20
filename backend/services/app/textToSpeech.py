from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
from abc import ABC, abstractmethod
import pyttsx3
import time

# TODO
# 1. find a better model


class googleTextToSpeech():

    def text_to_speech(self, text:str):
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
        # return audio_data
        return

class pyTextToSpeech():

    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', self.rate-20)
       

    def text_to_speech(self, text:str, voice:str = None):
            # self.engine.setProperty('voice', voice)
            self.engine.say(text)
            self.engine.runAndWait()
            return
        
if __name__ == "__main__":
    # Define text and description
    text_prompt = """
Exactly! And the distillation part is where you take a LARGE-model,and compress-it down into a smaller, more efficient model that can run on devices with limited resources.
"""
    description = """
Laura's voice is expressive and dramatic in delivery, speaking at a fast pace with a very close recording that almost has no background noise.
"""

    # parlerTextToSpeech(description=description,
    #                    device="cpu",
    #                    ).text_to_speech(text_prompt)
    
    # start_time = time.time()
    # GoogleTextToSpeech().text_to_speech(text_prompt) 
    # end_time = time.time()
    # print(f"Gtts Time taken: {end_time - start_time} seconds")

    eng = pyTextToSpeech()
    # for voice in eng.voices:
    #     print(voice)
    #     eng.text_to_speech(text_prompt, voice.name)
    eng.text_to_speech(text_prompt, "com.apple.speech.synthesis.voice.Alex")
        
