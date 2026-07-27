# 🌿 Edge AI-Based Multiclass Tomato Leaf Disease Classification using YOLOv8 on Raspberry Pi

## 📌 Project Overview

This project presents an Edge AI-based system for real-time multiclass tomato leaf disease classification using YOLOv8, Raspberry Pi, OpenCV, and Flask.

The system captures live images from a USB camera, performs on-device inference using a trained YOLOv8 classification model, and predicts the health condition of tomato leaves without requiring an internet connection. The solution is designed for portable agricultural monitoring and enables farmers to identify diseases quickly in real time.

---

## 🎯 Objectives

- Develop an offline tomato disease classification system
- Deploy AI inference on Raspberry Pi
- Perform real-time image classification using YOLOv8
- Monitor environmental conditions using a DHT11 sensor
- Provide a lightweight and low-cost precision agriculture solution

---

## 🌱 Diseases Classified

The model classifies the following tomato leaf conditions:

- Tomato Bacterial Spot
- Tomato Early Blight
- Tomato Late Blight
- Tomato Leaf Mold
- Tomato Septoria Leaf Spot
- Tomato Spider Mites
- Tomato Target Spot
- Tomato Yellow Leaf Curl Virus
- Tomato Mosaic Virus
- Healthy Tomato Leaf

---

## 🛠 Hardware Used

- Raspberry Pi
- USB Camera
- DHT11 Temperature & Humidity Sensor
- MicroSD Card
- Power Supply

---

## 💻 Software & Libraries

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- Flask
- PyTorch
- NumPy
- Adafruit DHT Library

---

## ⚙️ Project Workflow

1. Capture tomato leaf image using USB camera
2. Read environmental data from DHT11 sensor
3. Process image using OpenCV
4. Perform inference using trained YOLOv8 model
5. Predict disease category
6. Display prediction locally and through a Flask web interface

---

## 📊 Model Training

Model: YOLOv8 Nano Classification (yolov8n-cls)

Training Configuration:

- Epochs: 10
- Image Size: 128 × 128
- Batch Size: 16
- Device: CPU
- Transfer Learning: Enabled

---

## 📈 Results

- Top-1 Validation Accuracy: ~97%
- Top-5 Validation Accuracy: ~100%

The model demonstrates strong classification performance across multiple tomato diseases while remaining lightweight enough for edge deployment.

---

## 🌐 Web Interface

A Flask-based web application streams real-time predictions from the Raspberry Pi, allowing users to monitor disease classifications directly through a browser.

---

## 📂 Project Structure

```
Edge-AI-Based-Multiclass-Tomato-Disease-Classification
│
├── assets/
│   ├── images
│
├── models/
│   └── best.pt
│   └── last.pt
├── src/
│   ├── capture_images.py
│   ├── create_labels.py
│   ├── dht11_reader.py
│   ├── camera_testing_code.py
│   ├── local_detect.py
│   ├── live_detect.py
│   └── web_detect.py
│
└── README.md
```

---

## 🚀 Future Improvements

- TensorFlow Lite optimization
- Quantized edge deployment
- Mobile application integration
- Cloud dashboard
- Disease severity estimation
- Automatic treatment recommendation

---

## 👨‍💻 Author

**Sharon A**

Bachelor of Engineering (Electrical & Electronics Engineering)

Interested in:

- Machine Learning
- Computer Vision
- Embedded AI
- Edge Computing
- Deep Learning