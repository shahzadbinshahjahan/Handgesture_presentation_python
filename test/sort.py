import os

pathImages=sorted(os.listdir("output"),key=lambda x:(len(x),x))
print(pathImages)
