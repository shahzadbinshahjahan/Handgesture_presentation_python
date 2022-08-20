import cv2
import os
import sys

n=len(sys.argv)
print("Total arguments passed ",n);
print(sys.argv[1])
folderpath=sys.argv[1]

imageList=sorted(os.listdir(folderpath),key=lambda x:(len(x),x))
print(imageList)
num=2
pathFullImage=os.path.join(folderpath,imageList[num])
img=cv2.imread(pathFullImage)
cv2.imshow("image",img)
cv2.waitKey(0)

