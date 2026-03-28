<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0a0f1e,50:3b0764,100:7c3aed&height=200&section=header&text=Hand%20Screen%20Controller&fontSize=42&fontColor=ffffff&fontAlignY=40&desc=Gesture-Based%20HCI%20%E2%80%A2%20Computer%20Vision%20%E2%80%A2%20Touch-Free%20Interaction&descAlignY=60&descSize=16&animation=fadeIn" />

<br/>

[![Python](https://img.shields.io/badge/Python-100%25-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://github.com/Bhogi123-T/Hand-Screen-controller)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://github.com/Bhogi123-T/Hand-Screen-controller)
[![MediaPipe](https://img.shields.io/badge/MediaPipe-Hand%20Tracking-0097A7?style=for-the-badge&logo=google&logoColor=white)](https://github.com/Bhogi123-T/Hand-Screen-controller)

[![Author](https://img.shields.io/badge/Author-Bhogeswara%20Rao%20T-7c3aed?style=flat-square)](https://github.com/Bhogi123-T)
[![Repo](https://img.shields.io/badge/GitHub-Hand--Screen--controller-181717?style=flat-square&logo=github)](https://github.com/Bhogi123-T/Hand-Screen-controller)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

</div>

---

## 📌 Overview

**Hand Screen Controller** is a gesture-based Human-Computer Interaction (HCI) system that lets you control your computer screen — move the cursor, click, scroll — using only your hand in front of a webcam. No mouse. No touch screen. Just your hand.

Built with OpenCV and MediaPipe, it tracks 21 hand landmarks in real time and maps their positions and gestures to system-level screen actions with minimal latency.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| ✋ Real-Time Hand Tracking | Detects and tracks 21 hand landmarks at high FPS via webcam |
| 🖥️ Touch-Free Screen Control | Move cursor, click, scroll — zero physical input required |
| 🎯 Accurate Gesture Detection | Distinguishes between distinct gestures for different screen actions |
| ⚡ Low-Latency Response | Optimized pipeline for near-instant reaction to hand movement |
| 🔒 No Hardware Required | Works with any standard webcam — no special sensors needed |

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 100% |
| Computer Vision | OpenCV |
| Hand Landmark Detection | MediaPipe |
| Screen Control | PyAutoGUI |
| Webcam Capture | cv2.VideoCapture |

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/Bhogi123-T/Hand-Screen-controller.git
cd Hand-Screen-controller

# Install dependencies
pip install opencv-python mediapipe pyautogui numpy

# Run the controller
python main.py
```

---

## 🤚 Gesture Controls

| Gesture | Action |
|---------|--------|
| ☝️ Index finger up | Move cursor |
| 👌 Pinch (thumb + index) | Left click |
| ✌️ Two fingers up | Scroll mode |
| ✊ Closed fist | Pause tracking |

---

## 🔄 How It Works

```
Webcam Feed (real-time)
        ↓
OpenCV Frame Capture
        ↓
MediaPipe Hand Landmark Detection (21 points)
        ↓
Gesture Classification Logic
        ↓
PyAutoGUI Screen Action
        ↓
Cursor Move / Click / Scroll
```

---

## ⚙️ Requirements

```
Python 3.7+
opencv-python
mediapipe
pyautogui
numpy
```

---

## 🤝 Contributing

Pull requests welcome. Extend with new gesture mappings or multi-hand support.

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:7c3aed,100:0a0f1e&height=100&section=footer&animation=fadeIn" />

**Built by [Bhogeswara Rao T](https://github.com/Bhogi123-T) · Chennai, India**

</div>
