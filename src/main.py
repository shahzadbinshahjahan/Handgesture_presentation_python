import cv2
import os
from handtrackingmodule import HandDetector

#variables
width,height=int(1366/2),int(768/2) #dimensions of webcam
folderPath="../Resources/test"
slideNumber=0
heightsmall,widthsmall=int(height/3),int(width/3) #dimensions of webcam on presentation
gestureThreshold=200
buttonPress=False
buttoncounter=0
buttondelay=20

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

imgNo=0
while True:
    success,img=cap.read()
    img=cv2.flip(img,1)
    #import images
    pathFullImage=os.path.join(folderPath,pathImages[slideNumber])
    currentSlide=cv2.imread(pathFullImage)


    hands,img=detector.findHands(img) #flipType=false will show the correctls hands, i.e left as left
    #drawing a line on the webcam so as to detect gestures only above that line
    cv2.line(img,(0,gestureThreshold),(width,gestureThreshold),(0,255,0),10)
    
    if hands and buttonPress is False:
        hand=hands[0] #get the first hand
        fingers=detector.fingersUp(hand)
        cx,cy=hand['center']
        #print(fingers )
        
        if cy<=gestureThreshold: #if hand is at the height of the face
            #Gesture-1 Go left
            if fingers == [1,0,0,0,0]: #thumb
                print("left")
                
                if slideNumber>0:
                    buttonPress=True
                    slideNumber-=1
            
            #Gesture -2 Go right
            if fingers == [0,0,0,0,1]: #little finger
                print("right")
                
                if slideNumber < len(pathImages)-1:
                    buttonPress=True
                    slideNumber+=1
    
    #Button pressed iterations
    if buttonPress:
        buttoncounter+=1
        if buttoncounter>buttondelay:
            buttoncounter=0
            buttonPress=False


    #overlay of webcam on presentation
    imgSmall=cv2.resize(img,(widthsmall,heightsmall))
    heigthCurrent,widthCurrent,_Current=currentSlide.shape
    currentSlide[0:heightsmall,widthCurrent-widthsmall:widthCurrent]=imgSmall
    
    cv2.imshow("Web Cam",img)
    cv2.imshow("Presentation",currentSlide)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

