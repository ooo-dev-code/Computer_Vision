import numpy as np
import cv2

cap = cv2.VideoCapture(0)

yellow = [0, 255, 255]
while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lowerLimit, upperLimit = get_limits(color=yellow)
    
    mask = cv2.inRange(hsv, lowerLimit, upperLimit)
    
    cv2.imshow('frame', mask)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()