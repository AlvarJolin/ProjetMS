import cv2
import time

class fps():
        
    def showFPS(self, img, pTime, cTime=0, draw=True, pos=(10, 70), policeType=cv2.FONT_HERSHEY_PLAIN, fontscale=3, color=(27, 39, 208), thickness=3):
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        
        if draw:
            cv2.putText(img, f'FPS: {str(int(fps))}', pos, policeType, fontscale, color, thickness)
        
        return pTime
        
        
        
def main():    
    pTime = 0  
    vid = cv2.VideoCapture(0)
    
    fpsClass = fps()    

    while True:
        success, img = vid.read()
        
        pTime = fpsClass.showFPS(img, pTime)
        
        cv2.imshow("Image", img)
        cv2.waitKey(1)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

if __name__ == '__main__':
    main()