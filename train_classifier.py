import os
import cv2
import mediapipe as mp
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

DATA_DIR = './data'

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True,
                       max_num_hands=1,
                       min_detection_confidence=0.5)

data = []
labels = []


for label in os.listdir(DATA_DIR):
    label_dir = os.path.join(DATA_DIR, label)
    for img_file in os.listdir(label_dir):
        img_path = os.path.join(label_dir, img_file)
        img = cv2.imread(img_path)
        if img is None:
            continue
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        result = hands.process(img_rgb)

        if result.multi_hand_landmarks:
            hand_landmarks = result.multi_hand_landmarks[0]
            x_list = [lm.x for lm in hand_landmarks.landmark]
            y_list = [lm.y for lm in hand_landmarks.landmark]
            data_aux = []

            for lm in hand_landmarks.landmark:
                data_aux.append(lm.x - min(x_list))
                data_aux.append(lm.y - min(y_list))

            data.append(data_aux)
            labels.append(label)

hands.close()

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)
model = RandomForestClassifier()
model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)
print(f"✅ Precisión del modelo: {accuracy*100:.2f}%")

# Guardar el modelo
with open('model.p', 'wb') as f:
    pickle.dump({'model': model, 'labels': sorted(set(labels))}, f)

print("✅ Modelo guardado como 'model.p'")
