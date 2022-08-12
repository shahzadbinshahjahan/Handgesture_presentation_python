import cv2
import mediapipe as mp
import time

class HandDetector():
    def __init__(self, mode=False, maxHands=2,detectionCon=0.5, trackCon=0.5):
        self.mode=mode
        self.maxHands=maxHands
        self.detectionCon=detectionCon
        self.trackCon=trackCon
        self.mpHands=mp.solutions.hands
        self.hands=self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.trackCon)
        self.mpDraw=mp.solutions.drawing_utils
    
    def findHands(self,img,draw=True):
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results=self.hands.process(imgRGB)
        #print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,handLms,self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self,img,handNo=0,draw=True):
        lmlist=[]
        if self.results.multi_hand_landmarks:
            myHand=self.results.multi_hand_landmarks[handNo]
            for id,lm in enumerate(myHand.landmark):
                #d stores the points of the landmarks
                #print(id,lm)
                #converting the decimal values of x and y
                h,w,c=img.shape
                cx,cy=int(lm.x*w),int(lm.y*h) #center point of each id
                #print(id,cx,cy) #prints all the values of 20 ids
                lmlist.append([id,cx,cy])
                if draw:
                   cv2.circle(img,(cx,cy),12,(255,0,255),cv2.FILLED)
        return lmlist

    
def main():
    pTime=0 #previous time
    cTime=0 #current time
    cap=cv2.VideoCapture(0)
    detector=HandDetector()
    while True:
        success,img=cap.read()
        img=detector.findHands(img) #draw=False will remove the mediapipe module drawing
        lmlist=detector.findPosition(img)
        if len(lmlist)!=0:
            print(lmlist[0])
        
        cTime=time.time()
        fps=1/(cTime-pTime)
        pTime=cTime

        cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
        cv2.imshow("Image",img)
        cv2.waitKey(1);


#so that if i run the code directly it shows what this module can do
if __name__=="__main__":
    main()