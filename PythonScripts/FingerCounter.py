import cv2
import FPS_Module
import HandTracking_Module as htm

pTime = 0
fpsClass = FPS_Module.fps()
wCam, hCam = 4000, 4000
sign = ''

vid = cv2.VideoCapture(0)
vid.set(3, wCam)
vid.set(4, hCam)

overLayList = []
    
detector = htm.handDetector(detectionConfidence=0.5)

while True:
    success, img = vid.read()
    
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        if lmList[3][2] > lmList[4][2]:
            pouceUp = True
        else:
            pouceUp = False
        
        if lmList[8][2] < lmList[6][2]:
            indexUp = True
        else:
            indexUp = False
        
        if lmList[12][2] < lmList[10][2]:
            majeurUp = True
        else:
            majeurUp = False
            
        if lmList[16][2] < lmList[14][2]:
            annulaireUp = True
        else:
            annulaireUp = False
            
        if lmList[20][2] < lmList[18][2]:
            auriculaireUp = True
        else:
            auriculaireUp = False
            
        #Vu camera
        if lmList[3][1] < lmList[4][1]:
            pouceRight = True
        else:
            pouceRight = False
        
        if lmList[8][1] > lmList[6][1]:
            indexRight = True
        else:
            indexRight = False
        
        if lmList[12][1] > lmList[10][1]:
            majeurRight = True
        else:
            majeurRight = False
            
        if lmList[16][1] > lmList[14][1]:
            annulaireRight = True
        else:
            annulaireRight = False
            
        if lmList[20][1] > lmList[18][1]:
            auriculaireRight = True
        else:
            auriculaireRight = False
            
            
        if pouceRight == indexRight == majeurRight == annulaireRight == auriculaireRight == indexUp == majeurUp == annulaireUp == auriculaireUp == True and pouceUp ==  False:
            sign = 'C'
        elif pouceRight == indexRight == majeurRight == annulaireRight == auriculaireRight == indexUp == majeurUp == annulaireUp == auriculaireUp == True:
            sign = 'M'
        elif pouceRight and indexUp == majeurUp == annulaireUp == auriculaireUp == False:
            sign = 'A'
        elif pouceRight == False and indexUp == majeurUp == annulaireUp == auriculaireUp == True:
            sign = 'B'
        elif indexUp == pouceRight == majeurRight == annulaireRight == auriculaireRight == True and majeurUp == annulaireUp == auriculaireUp == False:
            sign = 'D'
        elif pouceRight == indexUp == majeurUp == annulaireUp == auriculaireUp == False:
            sign = 'E'
        elif pouceUp == majeurUp == annulaireUp == auriculaireUp == True and indexUp == False:
            sign = 'F'
        elif indexUp == pouceUp == True and majeurUp == annulaireUp == auriculaireUp == pouceRight == False:
            sign = 'G'
        elif pouceRight == majeurUp == annulaireUp == False and indexUp == auriculaireUp == pouceUp == True:
            sign = 'H'
        elif pouceRight == majeurUp == annulaireUp == False and auriculaireUp == True:
            sign = 'I'
        elif pouceUp == indexRight == majeurRight == annulaireRight == True and auriculaireRight == False:
            sign = 'J'
        elif pouceUp == indexUp == majeurRight == True and annulaireRight == auriculaireRight == False:
            sign = 'K'
        elif pouceRight == indexUp == pouceUp == True and majeurUp == annulaireUp == auriculaireUp == False:
            sign = 'L'
        elif pouceRight == indexRight == majeurRight == True and annulaireRight == auriculaireRight == False:
            sign = 'N'
        
        
        else:
            sign = ''
    else:
        sign = ''
            
    
    
    pTime = fpsClass.showFPS(img, pTime)
    cv2.putText(img, sign, (1200, 100), cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 10)
    
    cv2.imshow("Image", img)
    cv2.waitKey(1)
