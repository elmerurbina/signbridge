import sys
import os

# Define the absolute path to the project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

# Ensure the model is loaded using the absolute path
model_path = os.path.join(BASE_DIR, 'model.p')

# Import necessary modules
from django.shortcuts import render
from django.http import StreamingHttpResponse

from inference_classifier import HandSignClassifier
from speech_to_sign import SpeechToSign

import cv2

# Initialize classifier and speech-to-sign converter
hand_classifier = HandSignClassifier(model_path=model_path)  # Pass model_path to the classifier
speech_to_sign = SpeechToSign()

def index(request):
    return render(request, 'communicator/index.html')

def generate_unified_frame():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.flip(frame, 1)
        frame, _ = hand_classifier.process_frame(frame)
        # You can add text like the recognized phrase if needed
        cv2.putText(frame, f"Voz: {speech_to_sign.last_recognized_phrase}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        _, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

def video_feed(request):
    return StreamingHttpResponse(generate_unified_frame(),
                                 content_type='multipart/x-mixed-replace; boundary=frame')
