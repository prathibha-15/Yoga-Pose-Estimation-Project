import streamlit as st
import cv2
import os
from joblib import load
from demo import correct_feedback
import mediapipe as mp

# Load the trained model
model = load("model.joblib")

# Initialize Mediapipe pose model and drawing utils
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_drawing = mp.solutions.drawing_utils

# Define the backend predict function for images
def predict(img_path, model, show=False):
    img = cv2.imread(img_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_rgb = cv2.resize(img_rgb, None, fx=0.5, fy=0.5)
    results = pose.process(img_rgb)
    
    if results.pose_landmarks:
        list_angles = extract_pose_angles(results)
        y = model.predict([list_angles])[0]
        
        # Draw landmarks and display the prediction
        mp_drawing.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.putText(img, str(y), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (215, 215, 0), 3)
        return img, y
    else:
        return img, "No landmarks detected"

# Streamlit app configuration
st.set_page_config(page_title="Yoga Pose Estimation", page_icon="🧘", layout="wide")

# Header and instructions
st.title("🧘 Yoga Pose Estimation")
st.markdown("### Upload a Video for Pose Estimation and Feedback")
st.write("Upload a video of your yoga pose, and our model will provide feedback on your posture to help you improve your alignment.")

# Sidebar with instructions
st.sidebar.title("How to Use")
st.sidebar.info("""
1. Upload a **clear and steady video** of your yoga pose.
2. Ensure **good lighting** and a **stable background** for best results.
3. Wait for the app to **process your video**.
4. Receive feedback and suggestions on improving your pose.
""")

# Initialize session state for processed video
if "output_video_path" not in st.session_state:
    st.session_state["output_video_path"] = None

# Upload Section
st.header("Upload Your Video")
uploaded_file = st.file_uploader("Choose a video file", type=["mp4", "avi", "mov"])

if uploaded_file is not None:
    # Show video preview
    st.video(uploaded_file)
    st.info("Processing your video. This may take a minute...")

    # Temporary file handling for video
    temp_video_path = "temp_video" + os.path.splitext(uploaded_file.name)[1]
    with open(temp_video_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Check if feedback has already been generated
    if st.session_state["output_video_path"] is None:
        # Progress bar for processing
        progress_bar = st.progress(0)
        st.text("Generating feedback...")

        # Generate feedback only once
        with st.spinner("Processing feedback..."):
            input_csv = r"C:\Users\prath\Desktop\YOGA PROJECT\teacher_yoga\angle_teacher_yoga.csv"
            output_video_path = "processed_video" + os.path.splitext(uploaded_file.name)[1]
            correct_feedback(model, video=temp_video_path, input_csv=input_csv, output_video=output_video_path)

            # Save the output path in session state
            st.session_state["output_video_path"] = output_video_path

        # Completion message after feedback generation
        st.success("Your video has been processed successfully! Feedback has been generated.")

 

# Download Section
if st.session_state["output_video_path"]:
    st.markdown("### Download Processed Video with Feedback")
    with open(st.session_state["output_video_path"], "rb") as file:
        video_data = file.read()
    st.download_button(
        label="Download Processed Video",
        data=video_data,
        file_name="processed_feedback_video.mp4",
        mime="video/mp4"
    )

# Footer Section
st.markdown("---")
st.markdown("### About This App")
st.write("""
This app uses machine learning to analyze yoga poses and provide real-time feedback to improve your form. 
Upload a video, and the model will evaluate your pose, providing feedback on your posture and offering suggestions for improvement.
""")
st.write("For more information or questions, feel free to reach out through our [GitHub](https://github.com).")

