import cv2
import mediapipe as mp
import FPS_Module

pTime = 0
fpsClass = FPS_Module.fps()

vid = cv2.VideoCapture(0)

mpPose = mp.solutions.pose
pose = mpPose.Pose(False, True)
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = vid.read()
    
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)
    
    if results.pose_landmarks:
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx = int(lm.x*w)
            cy = int(lm.y*h)
            if id == 0:
                cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
    
    pTime = fpsClass.showFPS(img, pTime)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
