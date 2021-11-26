import cv2
#adding the trained cascade file from paul viola
facecascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#Read our image
img = cv2.imread('many.jpg')
imgresize = cv2.resize(img,(400,300))
#convert image to grey scale to make it lighter
imgGrey = cv2.cvtColor(imgresize,cv2.COLOR_BGR2GRAY)

#Detecting the faces
faces = facecascade.detectMultiScale(imgGrey,1.1,3)

#loop through the detected faces
for(x,y,w,h) in faces:
    cv2.rectangle(imgresize,(x,y),(w+x,y+h),(255,0,0),2)

#display our image
cv2.imshow("resized",imgresize)
cv2.waitKey(0)