# 🖐 Detector de Lengua de Señas

Este proyecto es un **detector de lengua de señas** que combina visión por computadora y reconocimiento de voz para facilitar la comunicación entre personas con discapacidad auditiva y oyentes.

---

## 📚 Descripción

El programa tiene **dos marcos principales (frames)**, representando dos caras de la moneda:

✅ **Para la persona con discapacidad auditiva (persona especial):**  
Utilizando la webcam, el sistema reconoce la seña que realiza y traduce a qué letra o expresión corresponde.

✅ **Para la persona oyente (persona normal):**  
Mediante reconocimiento de voz, el sistema detecta lo que la persona dice y muestra en pantalla una imagen con la seña correspondiente, permitiendo que la persona especial comprenda el mensaje.

---

## 🎯 Objetivo

Este proyecto se presentará el **10 de mayo** en la **Feria de Matemáticas** de la **Universidad Nacional de Ingeniería (UNI), Centro Regional Juigalpa**.  
El propósito es demostrar que las matemáticas son fundamentales para el desarrollo de la inteligencia artificial, y que estos conocimientos pueden aplicarse en la vida real para resolver problemas complejos y generar un impacto positivo en la sociedad.

---

## ⚙️ Cómo funciona

El proyecto se desarrolla en **varias etapas** mediante diferentes scripts:

1️⃣ **Recolección de imágenes**  
Archivo: `collect_imgs.py`  
👉 Toma 100 fotos por cada letra del abecedario o expresión, usando la cámara.

2️⃣ **Creación del dataset**  
Archivo: `create_dataset.py`  
👉 A partir de las imágenes recolectadas, crea un dataset que servirá como base de información para entrenar el modelo.

3️⃣ **Entrenamiento del modelo**  
Archivo: `train_inference.py`  
👉 Usa los archivos `.pickle` generados en la etapa anterior para entrenar el modelo y generar el archivo final del modelo.

4️⃣ **Clasificación en tiempo real**  
Archivo: `inference_classifier.py`  
👉 Usa el modelo entrenado para reconocer el lenguaje de señas captado por la webcam.

5️⃣ **Reconocimiento de voz**  
Archivo: `speech_to_sign.py`  
👉 Reconoce frases habladas y muestra en pantalla la imagen de la seña correspondiente.

6️⃣ **Integración de ambos mundos**  
Archivo: `unified_frames.py`  
👉 Unifica los dos sistemas en dos marcos verticales, permitiendo que la persona normal y la persona especial puedan comunicarse de forma efectiva y fluida.

---

## 🛠 Tecnologías utilizadas

- [MediaPipe](https://mediapipe.dev/)  
- [OpenCV](https://opencv.org/)  
- `sounddevice==0.5.1`  
- `SpeechRecognition==3.14.2`  
- `scikit-learn`

---

## 🚀 Futuro

Se planea integrar este sistema en una plataforma web accesible para cualquier persona, ampliando su alcance y generando aún más impacto social.

---

## 📸 Ejemplo visual

![Ejemplo del sistema en uso](README_Ejemplo.png)

---

## 💡 Créditos

Proyecto desarrollado por [NicaDevs](https://github.com/NicaDevs) para la Feria de Matemáticas 2025.  
Contribuciones de: Elmer Urbina y Holman Rugama.

