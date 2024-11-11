import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    
    image = cv2.rectangle(frame, (0, 0), (width, height), (255, 0, 0), 10)
    image = cv2.line(image, (0, 0), (width, height), (255, 0, 0), 10)
    image = cv2.circle(image, (30, 30), 60, (255, 0, 0), 10)
    font = cv2.FONT_ITALIC
    image = cv2.putText(image, 'hi', (200, height-10), font, 4, (0, 255, 0), 5, cv2.LINE_AA)
    
    cv2.imshow('frame', image)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()