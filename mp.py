import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from PIL import Image

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils
pose = mp_pose.Pose(static_image_mode=True)

st.title("🧍 Pose Detection App")
st.write("Upload an image and this app will estimate the pose (Standing, Sitting, Lying).")

# Upload section
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

def classify_pose(landmarks):
    left_shoulder = landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value]
    left_hip = landmarks[mp_pose.PoseLandmark.LEFT_HIP.value]

    # Simple vertical distance between shoulder and hip
    vertical_distance = abs(left_shoulder.y - left_hip.y)

    if vertical_distance > 0.25:
        return "Standing"
    elif 0.1 < vertical_distance <= 0.25:
        return "Sitting"
    else:
        return "Lying or Unknown"

if uploaded_file:
    # Convert image to CV2 format
    image = Image.open(uploaded_file).convert('RGB')
    img_np = np.array(image)
    img = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # Pose estimation
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb_img)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        pose_label = classify_pose(results.pose_landmarks.landmark)

        # Display result
        st.success(f"Detected Pose: **{pose_label}**")
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption='Processed Image', use_column_width=True)
    else:
        st.warning("No pose detected.")
        st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption='Uploaded Image', use_column_width=True)
