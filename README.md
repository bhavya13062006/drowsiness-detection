# Driver Drowsiness Detection System

A real-time computer vision project that detects driver drowsiness using a webcam.  
The system tracks facial landmarks, monitors eye closure, and displays an alert when the driver appears drowsy.

---

## 1. Project Overview

Driver drowsiness is one of the major causes of road accidents. A tired driver may lose focus, react slowly, or even fall asleep while driving. This project is designed to reduce that risk by continuously monitoring the driver's eyes through a webcam.

The system uses **MediaPipe Face Mesh** to detect facial landmarks and **OpenCV** to capture and process video frames. It calculates the **Eye Aspect Ratio (EAR)** to determine whether the eyes are open or closed. If the eyes remain closed for a fixed number of consecutive frames, the system triggers a drowsiness alert.

---

## 2. Objective

The main objective of this project is to build a simple and meaningful safety system that can:

- detect a driver's face in real time
- monitor eye movement continuously
- identify prolonged eye closure
- alert the driver when drowsiness is detected

---

## 3. Problem Statement

Many road accidents happen because drivers become tired or drowsy while driving. In such situations, the driver may not realize that they are losing alertness. A real-time drowsiness detection system can help by warning the driver before a dangerous situation occurs.

---

## 4. Proposed Solution

This project provides a webcam-based monitoring system that:

1. captures live video from the webcam
2. detects the driver's facial landmarks
3. extracts eye landmark points
4. calculates Eye Aspect Ratio (EAR)
5. checks whether the eyes stay closed for several frames
6. displays an alert when drowsiness is detected

This solution is simple, practical, and easy to demonstrate.

---

## 5. Technologies Used

- **Python** – programming language used to build the project
- **OpenCV** – used for video capture and display
- **MediaPipe** – used for facial landmark and eye point detection
- **NumPy** – used for numerical operations

---
## 6. Project Structure
```txt
drowsiness-detection/
├── src/
│   └── app.py
├── requirements.txt
├── README.md
