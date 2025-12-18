# People Detection and Counting using YOLOv8

## 📌 Project Overview
This project detects and counts the number of people present in an image using a pretrained YOLOv8 object detection model. The system reads an input image, identifies people, draws bounding boxes around detected individuals, and displays the total number of people detected. The project is implemented using Python, OpenCV, and runs in Google Colab without requiring any hardware.

---

## 🎯 Objectives
- To detect people in an image automatically using deep learning  
- To draw bounding boxes around detected individuals  
- To count the total number of people present in the image  
- To understand the application of pretrained models in computer vision  

---

## 🧠 About YOLOv8
YOLO (You Only Look Once) is a deep learning-based object detection algorithm that processes the entire image in a single forward pass. YOLOv8 is the latest version of YOLO, offering improved accuracy and speed. In this project, YOLOv8 is used to detect the **person** class from images.

---

## 🛠️ Technologies Used
- Python  
- OpenCV  
- YOLOv8 (Ultralytics)  
- Matplotlib  
- Google Colab  

---

## 💻 Methodology
- The input image is read using OpenCV  
- The pretrained YOLOv8 model (`yolov8n.pt`) is loaded  
- The model predicts objects in the image  
- Only detections belonging to the **person** class are selected  
- Bounding boxes are drawn around each detected person  
- The total number of people is counted and displayed  

---

## 🖼️ Output
- Green bounding boxes are drawn around detected people  
- The total number of people detected is shown on the image and printed in the console  

---

## ⚠️ Limitations
- Some people may not be detected in dense crowd images  
- Occlusion and small object sizes can reduce detection accuracy  
- Detection performance depends on image quality and lighting  

---

## 📚 Learning Outcomes
- Understanding object detection using YOLOv8  
- Practical use of pretrained deep learning models  
- Using OpenCV for image processing and visualization  
- Running computer vision projects in Google Colab  

---

## 🧑‍🎓 Academic Use
This project is intended for educational and academic purposes, including mini-projects and learning computer vision concepts.

---


