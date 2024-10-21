from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from io import BytesIO


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
    tts = gTTS(text=text, lang='en', )
    audio_data = BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    # Convert MP3 file to WAV format
    audio = AudioSegment.from_file(audio_data, format="mp3")
    play(audio) 
    return
if __name__ == "__main__":
    text_to_speech("Hello, Welcome to the world of text to speech conversion using Python.")
