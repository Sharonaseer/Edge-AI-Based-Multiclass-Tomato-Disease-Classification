from flask import Flask, Response
import cv2
from ultralytics import YOLO

app = Flask(__name__)

# Load YOLO model
model = YOLO("/home/raspberrypi/.pyenv/runs/classify/train7/weights/best.pt")

# Open camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not opened")
else:
    print("✅ Camera opened")

def generate_frames():
    while True:
        success, frame = cap.read()
        if not success:
            print("❌ Frame not captured")
            break

        results = model(frame)
        annotated_frame = results[0].plot()

        ret, buffer = cv2.imencode('.jpg', annotated_frame)
        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')


@app.route('/')
def index():
    return """
    <html>
    <body style="text-align:center;">
        <h1>Live Tomato Disease Detection</h1>
        <img src="/video" width="80%">
    </body>
    </html>
    """

@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
