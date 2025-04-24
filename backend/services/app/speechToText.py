
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

class OpenAIASR():

    def __init__(self):
        self.model = whisper.load_model("base")
        
    def record_audio(self, filename="input.wav", duration=30, fs=44100):
        # print("Recording...")
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()  # Wait until recording is finished
        write(filename, fs, audio)

    def speech_to_text(self):
        try:
            print("recording...")   
            self.record_audio("voice_input.wav")
            result = self.model.transcribe("voice_input.wav")
              
        ## except the future warning
        finally:
            # Clean up
            if os.path.exists("voice_input.wav"):
                os.remove("voice_input.wav")
        return result["text"]
      
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
import whisper
import sounddevice as sd
from scipy.io.wavfile import write

model = whisper.load_model("base")
  
if __name__ == "__main__":
    # Initialize the speech recognition class
    asr = OpenAIASR()
    
    # Call the speech_to_text method
    text = asr.speech_to_text()
    
    # Print the recognized text
    print("Recognized Text:", text)

    