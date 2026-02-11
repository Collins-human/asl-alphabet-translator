from flask import Flask, render_template, Response
import cv2
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)

# Load your trained model
model = load_model('asl_model_best_v2.h5')  # ← change to your best model file

# Class names (same order as training)
class_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z']

# Webcam capture
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Preprocess frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        resized = cv2.resize(gray, (64, 64))
        normalized = resized / 255.0
        input_img = normalized.reshape(1, 64, 64, 1)

        # Predict
        prediction = model.predict(input_img, verbose=0)
        predicted_idx = np.argmax(prediction)
        confidence = prediction[0][predicted_idx] * 100
        letter = class_names[predicted_idx]

        # Draw result
        text = f"{letter} ({confidence:.1f}%)"
        color = (0, 255, 0) if confidence > 70 else (0, 0, 255)
        cv2.putText(frame, text, (20, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 3)

        # Encode frame as JPEG
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)