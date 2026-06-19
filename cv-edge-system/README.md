Real-Time Object Detection on Edge Hardware

A live computer vision system that detects and classifies objects in real time using a webcam feed, built for the IoT \& Embedded Systems Intern Assessment.

Hardware Setup

This system was developed and tested on an HP EliteBook 830 G7 (AMD Ryzen 5 PRO 4650U) using its built-in webcam, rather than a Raspberry Pi. This substitution was made because no dedicated edge hardware (Raspberry Pi/SBC) was available at the time of this assessment. The laptop serves as an equivalent local-inference development environment, fully meeting the requirement that "a laptop or desktop processing a live webcam stream is acceptable, provided the substitution is clearly justified."

Model

YOLOv8n (nano) from the Ultralytics library was selected for this project:



Runs efficiently on CPU without requiring a GPU

Lightweight (\~6MB) with fast inference suitable for real-time detection

Pretrained on the COCO dataset (80 object classes), requiring no custom training

Good balance of speed vs. accuracy for live demonstration purposes



Dataset

The pretrained COCO dataset is used, which includes 80 everyday object classes (person, cell phone, bottle, laptop, cup, etc.). This was chosen over a custom dataset because it:



Requires no data collection or labeling effort

Is immediately demonstrable with common objects

Still satisfies the "at least two distinct object classes" requirement (e.g., person + cell phone)



How It Works



Captures a continuous live feed from the webcam using OpenCV

Runs YOLOv8n inference on each frame

Draws bounding boxes, class labels, and confidence scores on detected objects

Displays an FPS counter to monitor real-time performance

Press Q to quit the application



Installation

pip install -r requirements.txt

Usage

Run with default webcam:



python main.py

Run with a different camera index if webcam isn't detected on index 0:



python main.py --source 1

Filter specific classes, e.g. only person and cell phone:



python main.py --classes 0 67

Adjust confidence threshold:



python main.py --conf 0.5

Project Structure

cv-edge-system folder contains:



main.py - Entry point: camera loop, inference, display



requirements.txt - Python dependencies



README.md - Documentation



utils folder containing:



init.py



draw.py - Draws bounding boxes, labels, confidence scores



fps.py - Rolling FPS counter

Design Decisions and Trade-offs



Laptop vs. Raspberry Pi: Chose laptop CPU inference over Raspberry Pi due to hardware availability, accepting higher power draw in exchange for faster development iteration and more reliable real-time performance.

YOLOv8n vs. larger YOLO variants: Chose the nano variant for real-time CPU performance over the higher accuracy of larger variants (YOLOv8s/m/l), since real-time responsiveness was prioritized for a live demo.

Pretrained COCO vs. custom dataset: Chose pretrained weights to maximize reliability and turnaround time given the assessment timeline, at the cost of not demonstrating custom dataset/fine-tuning skills.



Author

Saad Ejaz — Computer Engineering student, Pak-Austria Fachhochschule (PAF-IAST)

