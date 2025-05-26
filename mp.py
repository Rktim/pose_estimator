import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from PIL import Image
import math

def calculate_angle(a, b, c):
    """Calculate angle between three points (in degrees)."""
    a = np.array(a)  # First point
    b = np.array(b)  # Middle point
    c = np.array(c)  # End point
    
    ba = a - b
    bc = c - b
    
    cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
    angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
    
    return np.degrees(angle)

def classify_pose(landmarks, img_shape):
    """
    Classify pose as standing, sitting or lying using landmarks.
    landmarks: normalized landmarks from mediapipe
    img_shape: (height, width)
    """
    h, w = img_shape

    # Get landmark points in pixel coordinates
    def get_point(id):
        lm = landmarks.landmark[id]
        return int(lm.x * w), int(lm.y * h)

    # Points of interest
    left_hip = get_point(mp_pose.PoseLandmark.LEFT_HIP.value)
    left_knee = get_point(mp_pose.PoseLandmark.LEFT_KNEE.value)
    left_ankle = get_point(mp_pose.PoseLandmark.LEFT_ANKLE.value)
    left_shoulder = get_point(mp_pose.PoseLandmark.LEFT_SHOULDER.value)

    # Calculate angles
    knee_angle = calculate_angle(left_hip, left_knee, left_ankle)
    hip_angle = calculate_angle(left_shoulder, left_hip, left_knee)

    # Vertical distances (y-axis)
    hip_y = left_hip[1]
    knee_y = left_knee[1]
    shoulder_y = left_shoulder[1]

    # Heuristic rules
    if hip_y < knee_y and abs(hip_angle - 180) < 30:
        return "Standing"
    elif abs(hip_y - knee_y) < 30 and knee_angle < 140:
        return "Sitting"
    elif abs(shoulder_y - hip_y) < 30:
        return "Lying down"
    else:
        return "Unknown posture"

# Initialize MediaPipe Pose globally
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

st.title("🧍‍♂️ Pose Estimator with Posture Classification")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    img = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    h, w, _ = img.shape

    with mp_pose.Pose(static_image_mode=True) as pose:
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(rgb)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            posture = classify_pose(results.pose_landmarks, (h, w))
            st.success(f"Posture detected: **{posture}**")
        else:
            st.warning("No pose detected.")

    st.image(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), caption="Processed Image", use_container_width=True)
else:
    st.info("Please upload an image to begin.")
