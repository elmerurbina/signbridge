import cv2
import threading
import numpy as np
from inference_classifier import HandSignClassifier
from speech_to_sign import SpeechToSign

hand_classifier = HandSignClassifier()
speech_to_sign = SpeechToSign()

# Variable para mostrar estado de audio en tiempo real
audio_status = "Esperando entrada de voz..."

def audio_thread():
    global audio_status
    while True:
        audio_status = "Escuchando..."
        result = speech_to_sign.listen_and_update()
        if result:
            audio_status = f"Frase reconocida: {speech_to_sign.last_recognized_phrase}"
        else:
            audio_status = "No se reconoció frase. Intentando nuevamente..."

audio_listener = threading.Thread(target=audio_thread, daemon=True)
audio_listener.start()

cap = cv2.VideoCapture(0)
print("Iniciando cámara. Presiona 'Q' para salir.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo acceder a la camara.")
        break

    frame = cv2.flip(frame, 1)
    processed_frame, predicted_label = hand_classifier.process_frame(frame)

    left_frame = processed_frame.copy()
    cv2.putText(left_frame, "Persona Especial", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Mostrar imagen de signo
    if speech_to_sign.last_sign_image is not None:
        sign_image_resized = cv2.resize(speech_to_sign.last_sign_image, (150, 150))
        h, w, _ = sign_image_resized.shape
        left_frame[10:10 + h, left_frame.shape[1] - w - 10:left_frame.shape[1] - 10] = sign_image_resized

    right_frame = np.zeros_like(left_frame)
    cv2.putText(right_frame, "Persona Normal", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Mostrar estado de audio (actualizado)
    cv2.putText(right_frame, audio_status, (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Mostrar estado de mano
    if predicted_label is None:
        cv2.putText(right_frame, "No se detecto expresion de mano.", (10, 140),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    else:
        cv2.putText(right_frame, f"Expresion detectada: {predicted_label}", (10, 140),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    combined_frame = cv2.hconcat([left_frame, right_frame])
    cv2.imshow("Clasificador Unificado (Mano + Voz)", combined_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
