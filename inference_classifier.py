import pickle
import cv2
import mediapipe as mp
import numpy as np

class HandSignClassifier:
    def __init__(self, model_path='model.p'):
        with open(model_path, 'rb') as f:
            model_dict = pickle.load(f)
        self.model = model_dict['model']
        self.labels = model_dict['labels']


        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

    def process_frame(self, frame):
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        predicted_label = None

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

                x_list = [lm.x for lm in hand_landmarks.landmark]
                y_list = [lm.y for lm in hand_landmarks.landmark]
                data_aux = []

                for lm in hand_landmarks.landmark:
                    data_aux.append(lm.x - min(x_list))
                    data_aux.append(lm.y - min(y_list))

                prediction = self.model.predict([np.asarray(data_aux)])
                predicted_label = prediction[0]

        else:
            cv2.putText(frame, "No se detecto mano", (10, 100),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        return frame, predicted_label
