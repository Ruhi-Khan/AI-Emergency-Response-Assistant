from ultralytics import YOLO
from PIL import Image

model = YOLO("yolov8n.pt")

def detect_objects(image_file):
    img = Image.open(image_file)
    results = model(img)

    detected = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            detected.append(model.names[cls])

    return detected