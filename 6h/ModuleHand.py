import time
import numpy
import cv2
import mediapipe as mp

class handDetector():
    def __init__(self, mode=False, maxHands=3,complexity=1, detectionCon=0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.complexity = complexity
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.complexity, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

        
    def findHands(self, img, draw=True):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:   
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    
        return img
    
    def findPositions(self, img, handNo=0, draw=True):

        imgRGB2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results2 = self.hands.process(imgRGB2)
        
        lmList = []
        if self.results2.multi_hand_landmarks:
            myHand = self.results2.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                # if draw:
                #     cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                                        
        return lmList
    
    def game(self, img, top_finger_posX, top_finger_posY, window_width, window_height):
        font = cv2.FONT_ITALIC
        
        if not top_finger_posX < 200 and top_finger_posY < 300:
            print("Button Clicked !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!") 
            img = cv2.rectangle(img, (0, 0), (window_width, window_height//5), (0, 0, 0), -1)
            start = cv2.putText(img, 'Start', (window_width, window_height//6), font, 4, (255, 0, 0), 5, cv2.LINE_AA)
    
def main():
    
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    
    while True:
        width = int(cap.get(3))
        height = int(cap.get(4))
        success, img = cap.read()
        gray_flip = cv2.flip(img,1)
        lmList = detector.findPositions(img)
        if len(lmList) !=0:
            if lmList[8][2] < lmList[6][2]:
                
                start_game = detector.game(img, lmList[8][1], lmList[8][2], window_width=width, window_height=height)
                img = detector.findHands(img)
                cv2.circle(img, (lmList[8][1], lmList[8][2]), 15, (255, 112, 255), cv2.FILLED)
                print(lmList[8][0], lmList[8][1], lmList[8][2])
        else:
            print("No hands found")
        
        
        cv2.imshow('Image', img)
    
        if cv2.waitKey(1) == ord('q'):
            break
        
if __name__ == "__main__":
    main() 
