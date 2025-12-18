import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
import os

# -------------------------------
# Configuration
# -------------------------------
IMAGE_PATH = "People 2.jpg"   # change to your image file name
CONF_THRESHOLD = 0.25

# -------------------------------
# Load YOLOv8 model
# -------------------------------
model = YOLO("yolov8n.pt")

# -------------------------------
# Read image
# -------------------------------
image = cv2.imread(IMAGE_PATH)

if image is None:
    raise FileNotFoundError(
        f"Image not found at path: {IMAGE_PATH}"
    )

# Convert BGR to RGB
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# -------------------------------
# Run detection
# -------------------------------
results = model(IMAGE_PATH)

people_count = 0

# -------------------------------
# Process results
# -------------------------------
for result in results:
    for box in result.boxes:
        class_id = int(box.cls[0])
        confidence = float(box.conf[0])

        # Class 0 = person
        if class_id == 0 and confidence > CONF_THRESHOLD:
            people_count += 1

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

            cv2.putText(
                image,
                f"Person {confidence:.2f}",
                (x1, y1 - 8),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

# -------------------------------
# Display output
# -------------------------------
plt.figure(figsize=(10, 6))
plt.imshow(image)
plt.axis("off")
plt.title(f"People Detected: {people_count}")
plt.show()

print("Total people detected:", people_count)
