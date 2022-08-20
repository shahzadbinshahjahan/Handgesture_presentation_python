import cv2
import os
import numpy as np
from handtrackingmodule import HandDetector

#variables
width,height=int(1366),int(768) #dimensions of webcam
folderPath="../Resources/test"
slideNumber=0
heightsmall,widthsmall=int(height/5),int(width/5) #dimensions of webcam on presentation
gestureThreshold=300
buttonPress=False
buttoncounter=0
buttondelay=10 #fps
annotations=[[]] #stores at points to draw at
annotationnumber=-1
annotationstart=False

#camera setup
cap=cv2.VideoCapture(1) # 0 for webcam, 4 for phone cam
cap.set(3,width)
cap.set(4,height)

#get list of prensentation images
#fix::10.png not working even if key=len
#maybe it is storing as string, convert it to integer
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
    heigthCurrent,widthCurrent,_Current=currentSlide.shape


    hands,img=detector.findHands(img) #flipType=false will show the correctls hands, i.e left as left
    #drawing a line on the webcam so as to detect gestures only above that line
    cv2.line(img,(0,gestureThreshold),(width,gestureThreshold),(0,255,0),10)
    
    if hands and buttonPress is False:
        hand=hands[0] #get the first hand
        fingers=detector.fingersUp(hand)
        cx,cy=hand['center']
        #print(fingers )
        lmList=hand['lmList']

        #constrain values for easier drawing
        
        xVal=int(np.interp(lmList[8][0],[width//2,widthCurrent],[0,width]))
        yVal=int(np.interp(lmList[8][1],[150,height-150],[0,height]))
        indexFinger=xVal,yVal
        if cy<=gestureThreshold: #if hand is at the height of the face
            #Gesture-1 Go left
            if fingers == [1,0,0,0,0]: #thumb
                print("left")
                
                if slideNumber>0:
                    buttonPress=True
                    slideNumber-=1
                    annotations=[[]] #stores at points to draw at
                    annotationnumber=-1
                    annotationstart=False
            
            #Gesture -2 Go right
            if fingers == [0,0,0,0,1]: #little finger
                print("right")
                
                if slideNumber < len(pathImages)-1:
                    buttonPress=True
                    slideNumber+=1
                    annotations=[[]] #stores at points to draw at
                    annotationnumber=-1
                    annotationstart=False
            
        #Gesture -3 Show pointer
        if fingers == [0,1,1,0,0]: #index finger
            cv2.circle(currentSlide,indexFinger,8,(0,0,255),cv2.FILLED)

        #Gesture -4 Draw
        if fingers == [0,1,0,0,0]:
            if annotationstart == False:
                annotationstart = True
                annotationnumber+=1
                annotations.append([])
            cv2.circle(currentSlide,indexFinger,8,(0,0,200),cv2.FILLED)
            annotations[annotationnumber].append(indexFinger)
        else: 
            annotationstart=False
        
        #Gesture -5 Erase
        if fingers == [0,1,1,1,0]:
            if annotations:
                annotations.pop(-1)
                annotationnumber-=1
                buttonPress=True

    #Button pressed iterations
    if buttonPress:
        buttoncounter+=1
        if buttoncounter>buttondelay:
            buttoncounter=0
            buttonPress=False
    
    #draw at the points stored in annotations
    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j!=0:
                cv2.line(currentSlide,annotations[i][j-1],annotations[i][j],(200,0,0),6)
    
    #overlay of webcam on presentation
    imgSmall=cv2.resize(img,(widthsmall,heightsmall))
    currentSlide[0:heightsmall,widthCurrent-widthsmall:widthCurrent]=imgSmall
    
    cv2.imshow("Web Cam",img)
    cv2.imshow("Presentation",currentSlide)
    key=cv2.waitKey(1)
    if key==ord('q'):
        break
