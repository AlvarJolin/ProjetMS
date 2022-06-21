import cv2
import mediapipe as mp
import FPS_Module

class poseDetector():
    def __init__(self, mode=False, upBody=False, smooth=True, detectionConfidence=0.5, trackConfidence=0.5):
        self.mode = mode
        self.upBody = upBody
        self.smooth = smooth
        self.detectionConfidence = detectionConfidence
        self.trackConfidence = trackConfidence
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(False, True)
        
    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS, self.mpDraw.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2), self.mpDraw.DrawingSpec(color=(234, 8, 255), thickness=2, circle_radius=2))
        return img
    
    def findPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList


def main():
    pTime = 0
    
    vid = cv2.VideoCapture(0)
    
    detector = poseDetector()
    fpsClass = FPS_Module.fps()

    while True:
        success, img = vid.read()
        
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        
        '''
        if len(lmList) != 0:
            print(lmList[4])
        '''
        
        pTime = fpsClass.showFPS(img, pTime)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



if __name__ == '__main__':
    main()