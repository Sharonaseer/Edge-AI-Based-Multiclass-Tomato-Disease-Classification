import cv2
import time
import board
import adafruit_dht

dhtDevice = adafruit_dht.DHT11(board.D17)
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    humidity = dhtDevice.humidity

    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("USB Camera", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
