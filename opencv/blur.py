import cv2
import numpy as np

img = cv2.imread("person.jpg") #storing the image as a variable
imgResiz = cv2.resize(img,(400,300))
kernel = np.ones((5,5), np.uint8)# numpy array of dimension 5*5 unassigned integer of 8 bits

imgGray = cv2.cvtColor(imgResiz, cv2.COLOR_BGR2GRAY) # makes an object grey
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #makes an object blur
imgCanny = cv2.Canny(imgResiz, 100, 100)# shows the edges on a photo
imgDialation = cv2.dilate(imgCanny, kernel, iterations =1)
imgEroded = cv2.erode(imgDialation,kernel,iterations = 1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Real Image", img)
cv2.imshow("Canny Image", imgCanny)
cv2.imshow("Dilation Image", imgDialation)
cv2.imshow("Eroded Image", imgEroded)
cv2.waitKey(0)