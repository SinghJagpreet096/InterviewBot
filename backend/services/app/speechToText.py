
import speech_recognition as sr

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

if __name__ == "__main__":
    speech_to_text()
