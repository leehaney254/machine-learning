import cv2
import numpy as np

img = cv2.imread("cards.jpg")
imgresize = cv2.resize(img,(400,300))# resizing the image to make it smaller

width,height = 250,350
pos = np.float32([[1411,2275],[1400,3133],[2409,3082],[2265,2217]])# Points on the image to wrapp
pos2 = np.float32([[0,0],[0,height],[width,height],[width,0]])# How to wrap it
matrix = cv2.getPerspectiveTransform(pos,pos2)#Transforms the image
imgout = cv2.warpPerspective(img,matrix,(width, height))


cv2.imshow("Image", imgresize)
cv2.imshow("output", imgout)
cv2.waitKey(0)