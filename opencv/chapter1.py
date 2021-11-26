import cv2

"""
#Reading and outputing an image
img = cv2.imread("colors.jpg")# reading an image
cv2.imshow("ouptut", img)# displaying the image
cv2.waitKey(0)#setting delay for the image
"""

#Reading and outputing a video
#cap = cv2.VideoCapture("soldiers.mp4") #reading a video  to use camera webcam we use value 0

cap = cv2.VideoCapture(0)
cap.set(3,640) #setting width that is denoted by 3
cap.set(4,480) #Setting height that is denoted by 4
cap.set(10,500) #setting brightness denoted by 10

while True:
 success, img = cap.read() #displays a boolean if the video was successfully read or not, retuns specific no of bytes
 cv2.imshow("video", img)# outputs the video
 if cv2.waitKey(1) & 0xFF == ord('q'): #converts input reaad into 8 bits
   break
