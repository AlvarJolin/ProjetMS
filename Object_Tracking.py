from typing import Annotated
import cv2
import mediapipe as mp
import FPS_Module
from glob import glob
import object_detection

objectdetection=mp.solutions.object_detection
drawing=mp.solutions.drawing_utils
imagefiles=glob("./Sexypics/*")
with objectdetection.ObjectDetection(min_detection_confidence=0.5) as object_detection:
    for idx,file in enumerate(imagefiles):
        image=cv2.imread(file)
        image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        results=object_detection.process(image)
        if not results.detections:
            continue
        annotate_image=image.copy()
        for detection in results.detections:
            drawing.draw_detection(annotate_image, detection)
        cv2.imwrite("bonjour.png", annotate_image)