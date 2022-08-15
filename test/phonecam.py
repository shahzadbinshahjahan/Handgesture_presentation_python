import cv2

cap=cv2.VideoCapture(4)
while True:
    success,img=cap.read()
    cv2.imshow("Webcam",img)
    cv2.waitKey(1)

