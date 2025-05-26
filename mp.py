import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from PIL import Image

st.title("🧍‍♂️ Human Pose Estimator")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load the image using PIL and convert to OpenCV format
    image = Image.open(uploaded_file)
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    # Initialize MediaPipe Pose
    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils
    pose = mp_pose.Pose()

    # Convert BGR to RGB
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)

    # Draw landmarks
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        st.success("Pose detected successfully!")
    else:
        st.warning("No pose detected.")

    # Show the image (in RGB format)
    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Processed Image", use_container_width=True)

else:
    st.info("Please upload an image to begin.")
