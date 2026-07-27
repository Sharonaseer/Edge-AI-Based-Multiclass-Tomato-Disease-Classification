import cv2
import os
import time

save_path = "dataset/images/train"
os.makedirs(save_path, exist_ok=True)

cap = cv2.VideoCapture(0)

count = 0

print("Capturing images every 2 seconds. Press CTRL+C to stop.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera error")
        break

    filename = f"{save_path}/image_{count}.jpg"
    cv2.imwrite(filename, frame)

    print("Saved:", filename)

    count += 1
    time.sleep(2)

cap.release()
