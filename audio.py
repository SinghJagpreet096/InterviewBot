import numpy as np
import pydub

# Define a class to handle audio processing
class AudioProcessor:
    def __init__(self):
        self.audio_frames = []

    def recv(self, frame):
        # Capture the audio frame
        audio = np.frombuffer(frame.to_ndarray(), np.int16)
        self.audio_frames.append(audio)
        return frame  # Returning the audio frame (to keep it flowing)

    # def save_audio(self, filepath="output_audio.wav"):
    #     # Combine audio frames and save as WAV file
    #     audio = np.concatenate(self.audio_frames)
    #     sound = pydub.AudioSegment(
    #         audio.tobytes(), 
    #         frame_rate=frame.sample_rate, 
    #         sample_width=2,  # 16-bit audio
    #         channels=1
    #     )
    #     sound.export(filepath, format="wav")
    #     self.audio_frames = []  # Reset after saving