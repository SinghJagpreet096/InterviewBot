import streamlit as st
from streamlit import session_state as ss
from streamlit_pdf_viewer import pdf_viewer
import streamlit as st
import random
import time
from services.app.textToSpeech import pyTextToSpeech
from threading import Thread




# Function to display user and AI messages with different alignments
def display_message(message, sender="Candidate"):
    if sender == "Candidate":
        # Right-aligned for User
        st.markdown(f"""
            <div style="
                text-align: right;
                border: 0.5px faded #e0e0e0; 
                border-radius: 10px; 
                padding: 10px; 
                margin-bottom: 10px; 
                background-color: #055B0A; 
                width: fit-content;
                margin-left: auto;">
                {message}<br>
            </div>
        """, unsafe_allow_html=True)
    else:
        # Left-aligned for AI Assistant
        st.markdown(f"""
            <div style="
                text-align: left;
                border: 0.5px faded #e0e0e0; 
                border-radius: 10px; 
                padding: 10px; 
                margin-bottom: 10px; 
                background-color: #4B4B4B; 
                width: fit-content;
                margin-right: auto;">
                <strong>{message}</strong><br>    
            </div>
        """, unsafe_allow_html=True)


def go_to_page(page:str):
    st.session_state.page = page

def add_message(role, message):
    ss.conversation.append({"sender":role, "message": message})

def speech_thread(text):
    """Run TTS in a separate thread."""
    engine = pyTextToSpeech()
    tts_thread = Thread(target=engine.text_to_speech, args=(text,))
    tts_thread.start()
    print("TTS thread started")


def response_generator(response:str = "Hello! I am your AI Assistant. I will be conducting your interview today."):
        speech_thread(response)
        for word in response.split():
            
            yield word + " "
            time.sleep(0.2)

def preview_documents(resume, job_description):

    with st.sidebar:
        if 'pdf_resume' not in ss:
            ss.pdf_resume = None

        if 'pdf_jd' not in ss:
            ss.pdf_jd = None

        # Assign uploaded files to session state
        if resume:
            ss.pdf_resume = resume

        if job_description:
            ss.pdf_jd = job_description
        st.write("PDF Preview")
        with st.expander("Click to view Resume", expanded=False):
            if ss.pdf_resume and ss.pdf_resume.type == 'application/pdf':
                binary_resume = ss.pdf_resume.getvalue()  # Get the binary content of the file
                pdf_viewer(input=binary_resume, width=400, height=550)  # Display the PDF
        with st.expander("Click to view Job Description", expanded=False):
            # Display PDF preview for job description if it's a PDF
            if ss.pdf_jd and ss.pdf_jd.type == 'application/pdf':
                binary_jd = ss.pdf_jd.getvalue()  # Get the binary content of the file
                pdf_viewer(input=binary_jd, width=400, height=550)  # Display the PDF

# import cv2
# import streamlit as st
# import tempfile
# import os


# st.title("Webcam Video Recorder in Streamlit")

# # Open webcam
# video_capture = cv2.VideoCapture(1)

# # Set properties for saving the video
# frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
# frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
# frame_rate = int(video_capture.get(cv2.CAP_PROP_FPS)) or 20  # Default to 20 FPS if unavailable

# # Create a temporary file for the video
# temp_video_file = tempfile.NamedTemporaryFile(delete=False, suffix=".avi")
# video_output_path = temp_video_file.name

# # Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# out = cv2.VideoWriter(video_output_path, fourcc, frame_rate, (frame_width, frame_height))

# # Create a placeholder for video display
# video_frame = st.empty()
# stop = st.button("Stop")

# # Display frames from webcam and save them to video file
# while video_capture.isOpened():
#     ret, frame = video_capture.read()
#     if not ret:
#         break

#     # Write the frame to the video file
#     out.write(frame)

#     # Convert the frame to RGB and display it
#     frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     video_frame.image(frame_rgb)

#     # Stop recording if the "Stop" button is pressed
#     if stop:
#         break

# # Release resources
# video_capture.release()
# out.release()

# st.write("Recording saved.")

# # Provide a download link for the saved video
# st.write("Download your recorded video:")
# st.download_button(
#     label="Download Video",
#     data=open(video_output_path, "rb").read(),
#     file_name="recorded_video.MOV",
#     # mime="video/quicktime",
# )

# # Optionally, delete the temporary file after download
# os.unlink(video_output_path)

