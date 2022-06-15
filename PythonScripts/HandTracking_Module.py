import cv2
import mediapipe as mp
import FPS_Module

pTime = 0
fpsClass = FPS_Module.fps()

class handDetector():
    def __init__(self, mode=False, maxHands=2, modelComplexity=1, detectionConfidence=0.5, trackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.modelComplexity = modelComplexity
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionConfidence, self.trackConfidence)
        self.mpDraw = mp.solutions.drawing_utils
        
        
    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    
        return img
    
    
    def findPosition(self, img, handNumber=0, draw=True):
        
        lmList = []
        if self.results.multi_hand_landmarks:
            handUsed = self.results.multi_hand_landmarks[handNumber]
            
            for id, lm in enumerate(handUsed.landmark):
                h, w, c = img.shape
                cx = int(lm.x*w)
                cy = int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
            
        return lmList



def main():
    pTime = 0
    
    vid = cv2.VideoCapture(0)
    
    detector = handDetector()

    while True:
        success, img = vid.read()
        
        img = detector.findHands(img)
        lmList = detector.findPosition(img, 0, False)
        if len(lmList) != 0:
            print(lmList[4])
        
        pTime = fpsClass.showFPS(img, pTime)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == '__main__':
    main()