import os
import cv2
import mediapipe as mp
import numpy as np
import pickle

DATA_DIR = './data'

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=True,
                       max_num_hands=1,
                       min_detection_confidence=0.5)

data = []
labels = []

for label in os.listdir(DATA_DIR):
    dir_path = os.path.join(DATA_DIR, label)
    if not os.path.isdir(dir_path):
        continue
    print(f"📁 Procesando letra: {label}")
    for img_file in os.listdir(dir_path):
        img_path = os.path.join(dir_path, img_file)
        img = cv2.imread(img_path)
        if img is None:
            continue
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            x_list = [lm.x for lm in hand_landmarks.landmark]
            y_list = [lm.y for lm in hand_landmarks.landmark]
            data_aux = []

            for lm in hand_landmarks.landmark:
                data_aux.append(lm.x - min(x_list))
                data_aux.append(lm.y - min(y_list))

            data.append(data_aux)
            labels.append(label)

with open('../data.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)

print("✅ Dataset guardado como 'data.pickle'")
