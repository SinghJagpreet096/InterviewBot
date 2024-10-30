import cv2
import streamlit as st
import tempfile
import os


def video_recorder():

    # Open webcam
    video_capture = cv2.VideoCapture(index=1)

    # Set properties for saving the video
    frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_rate = int(video_capture.get(cv2.CAP_PROP_FPS)) or 20  # Default to 20 FPS if unavailable

    # Create a temporary file for the video
    temp_video_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
    video_output_path = temp_video_file.name

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_output_path, fourcc, frame_rate, (frame_width, frame_height))

    # Create a placeholder for video display
    video_frame = st.empty()
    stop = st.button("Stop")

    # Display frames from webcam and save them to video file
    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if not ret:
            break

        # Write the frame to the video file
        out.write(frame)

        # Convert the frame to RGB and display it
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        video_frame.image(frame_rgb)

    # Stop recording if the "Stop" button is pressed
        if stop:
            break

# Release resources
    video_capture.release()
    out.release()

    st.write("Recording saved.")

    # Provide a download link for the saved video
    st.write("Download your recorded video:")
    st.download_button(
        label="Download Video",
        data=open(video_output_path, "rb").read(),
        file_name="recorded_video.mp4",
        # mime="video/quicktime",
    )

    # Optionally, delete the temporary file after download
    os.unlink(video_output_path)

if __name__ == "__main__":
    video_recorder()
