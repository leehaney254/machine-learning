import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)#zero creates a black image
print(img.shape)#Shows dimension

#img [:] = 255,0,0 #gives color to the shape
img [200:300,100:300] = 255,0,0 #creates a small image on a larger one

cv2.line(img,(0,0),(300,300),(0,255,0),3)
cv2.putText(img,"OpenCV",(300,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,150,0),1)

cv2.imshow("Black image",img)
cv2.waitKey(0)