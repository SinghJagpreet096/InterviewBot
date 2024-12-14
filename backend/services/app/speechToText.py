
import speech_recognition as sr
import wave
import os

import warnings

# Suppress specific UserWarning from the moonshine library
warnings.filterwarnings(
    "ignore",
    category=UserWarning,
    module="moonshine",
)
# import moonshine

# TODO 
# 1. Find a better model

class speechRecognitionASR:
    
    def speech_to_text():
        # Initialize recognizer
        text = ""
        recognizer = sr.Recognizer()
        
        # Use the default microphone as the audio source
        with sr.Microphone() as source:
            print("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source)
            print("Listening...")
            
            # Capture the audio
            audio = recognizer.listen(source)
            
            try:
                # Recognize speech using Google Web Speech API
                print("Recognizing...")
                text = recognizer.recognize_google(audio)
                print("You said:", text)
            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Sorry, there was an error with the request; {e}")
        return text
    
# class moonshineASR:

#     def __init__(self) -> None:
#         # self.engine = moonshine()
#         self.model = 'moonshine/tiny'
#         self.recognizer = sr.Recognizer()

#     def speech(self):
#         with sr.Microphone() as source:
#             print("Adjusting for ambient noise...")
#             self.recognizer.adjust_for_ambient_noise(source)
#             print("Listening...")
            
#             # Capture the audio
#             audio = self.recognizer.listen(source)
#             with wave.open("recorded_audio.wav", "wb") as wav_file:
#                 wav_file.setnchannels(1)  # Mono audio
#                 wav_file.setsampwidth(2)  # 16-bit audio
#                 wav_file.setframerate(audio.sample_rate)
#                 wav_file.writeframes(audio.frame_data)  # Use frame_data instead of get_raw_data

#             return "recorded_audio.wav"
            
        
#     def speech_to_text(self):
#         audio = self.speech()
#         # print(audio) 
#         text = moonshine.transcribe(audio
#                                , model=self.model)
#         # delete the audio file
#         os.remove(audio)
#         return text
        
if __name__ == "__main__":
        # text = moonshineASR().speech_to_text()
        text = speechRecognitionASR.speech_to_text()
        print(text)

    