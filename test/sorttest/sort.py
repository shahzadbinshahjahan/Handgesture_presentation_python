import os

images=os.listdir("../output/")
pathImage=sorted(images,key=lambda x:(len(x),x))
print(pathImage)

#numbers = ['1','2','3','10','20','30']
#sortednumbers=sorted(numbers,key=int)
#print(sortednumbers)
