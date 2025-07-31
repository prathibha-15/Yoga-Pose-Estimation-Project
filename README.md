# 🧘‍♀️ Yoga Pose Estimation using Computer Vision

This is a real-time intelligent yoga posture guidance system that uses computer vision and pose detection to help users perform yoga asanas correctly. It utilizes **MediaPipe's Pose Estimation API** combined with **OpenCV** and a simple GUI to provide pose feedback, making it ideal for fitness applications and home workouts.

---

## 🔍 What Is It?

This project leverages landmark detection from video frames (via webcam) to identify body joints and analyze the user's posture in comparison to reference yoga poses. The key idea is to:

- 🧍‍♂️ Detect human body keypoints in real-time  
- 🧘 Classify poses like **Tadasana**, **Vrikshasana**, and **Warrior Pose**  
- 💬 Provide corrective feedback or validation to the user  

---

## 🚀 Features

- 🧘 Real-time yoga pose estimation from webcam  
- 📏 Landmark-based angle calculation and similarity checking  
- 🧠 Pose validation against reference images  
- 🖼️ Reference dataset images for common yoga asanas  
- 🖥️ Lightweight GUI using Tkinter  
- 💬 Feedback mechanism for accuracy and improvements  
- 🎯 Beginner-friendly and customizable  

---

## 🛠️ Tech Stack

- **Python** 🐍  
- **OpenCV** – Real-time video capture and image processing  
- **MediaPipe Pose** – Landmark detection with 33 key body points  
- **Tkinter** – For GUI window  
- **NumPy** – Angle and vector math  
- **Custom Dataset** – Sample images of correct poses  

---

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone https://github.com/prathibha-15/Yoga-Pose-Estimation-Project.git
cd Yoga-Pose-Estimation-Project

### 2. Install dependencies

```bash
pip install -r requirements.txt
### 3. Run the application

```bash
python main.py
---
