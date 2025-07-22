import cv2
import numpy as np
from inference_classifier import HandSignClassifier

classifier = HandSignClassifier()

def classify_hand_from_frame(frame_bytes: bytes):
    try:
        np_arr = np.frombuffer(frame_bytes, np.uint8)
        frame = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        if frame is None:
            print("❌ Error: No se pudo decodificar el frame.")
            return None

        frame = cv2.flip(frame, 1)
        processed_frame, label = classifier.process_frame(frame)

        if label:
            print(f"🟢 Gesto detectado: {label}")
        else:
            print("🔴 Ningún gesto detectado.")

        return label
    except Exception as e:
        print(f"❌ Excepción en classify_hand_from_frame: {e}")
        return None
