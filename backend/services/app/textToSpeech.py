from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO
from abc import ABC, abstractmethod
import IPython.display as ipd

# TODO
# 1. find a better model

class TextToSpeech(ABC):

    @abstractmethod
    def text_to_speech(self, text:str):
        pass
class GoogleTextToSpeech(TextToSpeech):

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

# class parlerTextToSpeech(TextToSpeech):
#     def __init__(self, description:str, device:str = "cpu"):
#         self.device = device
#         self.model = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler-tts-mini-v1").to(self.device)
#         self.tokenizer = ParlerTTSForConditionalGeneration.from_pretrained("parler-tts/parler-tts-mini-v1").to(self.device) 
#         self.description = description
        
#     def text_to_speech(self, text_prompt:str):
#         input_ids = self.tokenizer(self.description, return_tensors="pt").input_ids.to(self.device)
#         prompt_input_ids = self.tokenizer(text_prompt, return_tensors="pt").input_ids.to(self.device)
#         generation = self.model.generate(input_ids=input_ids, prompt_input_ids=prompt_input_ids)
#         audio_arr = generation.cpu().numpy().squeeze()
#         # Play audio in notebook
#         ipd.Audio(audio_arr, rate=self.model.config.sampling_rate)

        
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
    
    GoogleTextToSpeech().text_to_speech(text_prompt)    
    
        
