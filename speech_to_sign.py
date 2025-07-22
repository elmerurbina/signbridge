import speech_recognition as sr
import cv2
import numpy as np
import os
import time

class SpeechToSign:
    def __init__(self, sign_images_dir='./sign_imgs'):
        self.sign_images_dir = sign_images_dir
        self.phrase_to_image = {
            "hola": "HOLA.jpeg",
            "buenos días": "BUENOS_DIAS.png",
            "buenas noches": "BUENAS_NOCHES.jpg",
            "cómo estás": "COMO_ESTAS.png",
            "estoy bien gracias": "BIEN.png",
            "bien y tú": "BIEN_Y_TU.png",
            "mucho gusto": "MUCHO_GUSTO.png",
            "por favor": "POR_FAVOR.jpg",
            "adiós": "ADIOS.png"
        }
        self.recognizer = sr.Recognizer()
        self.last_sign_image = np.zeros((480, 640, 3), dtype=np.uint8)
        self.last_recognized_phrase = ""
        self.failed_attempts = 0

    def listen_and_update(self):
        try:
            with sr.Microphone() as source:
                print("🎤 Ajustando al ruido ambiental...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("🎤 Escuchando (5 seg)...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)

            text = self.recognizer.recognize_google(audio, language='es-ES').lower()
            print(f"🗣️ Dijiste: {text}")
            self.last_recognized_phrase = text

            matched = None
            for phrase in self.phrase_to_image:
                if phrase in text:
                    matched = phrase
                    break

            if matched:
                print(f"✔️ Frase reconocida: {matched}")
                img_path = os.path.join(self.sign_images_dir, self.phrase_to_image[matched])
                if os.path.exists(img_path):
                    img = cv2.imread(img_path)
                    img = cv2.resize(img, (640, 480))
                    self.last_sign_image = img
                    self.failed_attempts = 0
                else:
                    print(f"⚠️ Imagen no encontrada para '{matched}'")
                    self.last_sign_image = np.zeros((480, 640, 3), dtype=np.uint8)
            else:
                print("❓ Frase no reconocida en el conjunto disponible.")
                self.last_sign_image = np.zeros((480, 640, 3), dtype=np.uint8)
                self.failed_attempts += 1

            if self.failed_attempts >= 5:
                print("❌ Demasiados intentos fallidos. Deteniendo la grabación.")
                self.failed_attempts = 0
                self.last_sign_image = np.zeros((480, 640, 3), dtype=np.uint8)

        except sr.UnknownValueError:
            print("😕 No entendí lo que dijiste.")
            self.last_sign_image = np.zeros((480, 640, 3), dtype=np.uint8)
        except sr.RequestError:
            print("❌ Error con el servicio de reconocimiento de voz.")
            self.last_sign_image = np.zeros((480, 640, 3), dtype=np.uint8)
        except sr.WaitTimeoutError:
            print("⏰ Tiempo de espera agotado sin detectar voz.")
            self.last_sign_image = np.zeros((480, 640, 3), dtype=np.uint8)

        time.sleep(1)
