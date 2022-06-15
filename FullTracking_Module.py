import cv2
import mediapipe as mp
import FPS_Module

class fullDetector():
    def __init__(self, mode=False, maxHands=2, upBody=False, modelComplexity=1, smooth=True, detectionConfidence=0.5, trackConfidence=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.upBody = upBody
        self.modelComplexity = modelComplexity
        self.smooth = smooth
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.modelComplexity, self.detectionConfidence, self.trackConfidence)
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(False, True)
        self.mpDraw = mp.solutions.drawing_utils
        
        
    def findEverything(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.resultsHands = self.hands.process(imgRGB)
        self.resultsPose = self.pose.process(imgRGB)
        
        if self.resultsHands.multi_hand_landmarks:
            for handLms in self.resultsHands.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    
        if self.resultsPose.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.resultsPose.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
                    
        return img
    
    
    def findPosition(self, img, handNumber=0, draw=True):
        
        lmList = []
        if self.resultsHands.multi_hand_landmarks:
            handUsed = self.resultsHands.multi_hand_landmarks[handNumber]
            
            for id, lm in enumerate(handUsed.landmark):
                h, w, c = img.shape
                cx = int(lm.x*w)
                cy = int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 7, (255, 0, 255), cv2.FILLED)
        
        if self.resultsPose.pose_landmarks:
            for id, lm in enumerate(self.resultsPose.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
            
        return lmList



def main():
    pTime = 0
    
    vid = cv2.VideoCapture(0)
    
    detector = fullDetector()
    fpsClass = FPS_Module.fps()

    while True:
        success, img = vid.read()
        
        img = detector.findEverything(img)
        lmList = detector.findPosition(img, 0, False)
        
        pTime = fpsClass.showFPS(img, pTime)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == '__main__':
    main()
