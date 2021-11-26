import cv2

img =cv2.imread("Person.jpg")#Reading an image

print(img.shape)# Show dimensions of the image
imgResize = cv2.resize(img,(400,300))#We start with width then height

imgCropped = imgResize[0:200,200:500]#we start with height then width
#cv2.imshow("Real Image",img)#display the real image
cv2.imshow("resized Image",imgResize)
cv2.imshow("cropped Image", imgCropped)
cv2.waitKey(0)