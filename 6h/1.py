# General 

import numpy as np
import cv2
import  time
import mediapipe as mp

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms)
    
    cv2.imshow('frame', img)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
