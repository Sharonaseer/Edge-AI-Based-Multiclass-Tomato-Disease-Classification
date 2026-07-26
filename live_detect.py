from ultralytics import YOLO
import cv2

model = YOLO("/home/raspberrypi/.pyenv/runs/classify/train7/weights/best.pt")

cap = cv2.VideoCapture(2)

frame_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    annotated = results[0].plot()

    # save frame every loop
    filename = f"/home/raspberrypi/detect_{frame_count}.jpg"
    cv2.imwrite(filename, annotated)

    print("Saved:", filename)

    frame_count += 1

cap.release()
