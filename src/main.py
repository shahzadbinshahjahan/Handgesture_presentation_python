import cv2
import os
from handtrackingmodule import HandDetector

#variables
width,height=1280/2,720/2 #dimensions of webcam
folderPath="../Resources/test"
slideNumber=0
heightsmall,widthsmall=int(height/3),int(width/3) #dimensions of webcam on presentation

#camera setup
cap=cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

#get list of prensentation images
#fix::10.png not working even if key=len
pathImages=sorted(os.listdir(folderPath)) #sorting according to numbers and length
#print(pathImages)

#hand detector
detector=HandDetector(detectionCon=0.8,maxHands=1)

while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    #import images
    pathFullImage=os.path.join(folderPath,pathImages[slideNumber])
    currentSlide=cv2.imread(pathFullImage)

    hands,img=detector.findHands(img) #flipType=false will show the correct hands, i.e left as left
    if hands:
        hand=hands[0] #get the first hand
        fingers=detector.fingersUp(hand)
        print(fingers )

    #overlay of webcam on presentation
    imgSmall=cv2.resize(img,(widthsmall,heightsmall))
    heigthCurrent,widthCurrent,_Current=currentSlide.shape
    currentSlide[0:heightsmall,widthCurrent-widthsmall:widthCurrent]=imgSmall
    
    cv2.imshow("Web Cam",img)
    cv2.imshow("Presentation",currentSlide)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

