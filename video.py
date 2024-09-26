import cv2
import av

# Define a class to handle the video frame processing
class VideoRecorder:
    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")  # Convert frame to a NumPy array
        img_flipped = cv2.flip(img, 1)  # Flip the image horizontally (mirror)
        return av.VideoFrame.from_ndarray(img_flipped, format="bgr24")  # Convert back to VideoFrame
