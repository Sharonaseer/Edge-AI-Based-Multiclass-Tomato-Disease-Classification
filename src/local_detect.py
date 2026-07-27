import cv2
from ultralytics import YOLO
import time
import board
import adafruit_dht

model = YOLO("/home/raspberrypi/.pyenv/runs/classify/train7/weights/best.pt")
dhtDevice = adafruit_dht.DHT11(board.D17)

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("❌ Camera not opened")
    exit()
else:
    print("✅ Camera opened")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)
    frame = results[0].plot()

    cv2.imshow("YOLO Detection", frame)
    #temperature_c = dhtDevice.temperature
    #humidity = dhtDevice.humidity
    #temperature_f = temperature_c * 9/5 *32
    #cv2.putText(frame, humidity, (20,40),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    #print(f"Temp : {temperature_c:.1f} c/ {temperature_f:.1f} F | Humidity: {humidity:.1f}%")
    #cv2.imshow("YOLO Detection" ,frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
