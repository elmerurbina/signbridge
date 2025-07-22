import cv2
import numpy as np
from inference_classifier import HandSignClassifier


class VideoProcessor:
    def __init__(self, model_path='model.p'):
        self.classifier = HandSignClassifier(model_path=model_path)
        self.cap = None

    def start_capture(self):
        """Inicia la captura de video"""
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            raise RuntimeError("No se pudo abrir la cámara")
        return True

    def get_processed_frame(self):
        """Obtiene un frame procesado con la detección de señas"""
        ret, frame = self.cap.read()
        if not ret:
            return None, None

        frame = cv2.flip(frame, 1)
        processed_frame, label = self.classifier.process_frame(frame)
        return processed_frame, label

    def release(self):
        """Libera los recursos de la cámara"""
        if self.cap and self.cap.isOpened():
            self.cap.release()