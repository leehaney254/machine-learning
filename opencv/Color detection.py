import cv2
import numpy as np
path = 'redcar.jpg'

#create an empty function
def empty(a):
    pass

img= cv2.imread(path)

#creating a track bar to know the range value of the color
cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",640,240)
cv2.createTrackbar("Hue Min", "Trackbars",0,179,empty)
cv2.createTrackbar("Hue Max", "Trackbars",63,179,empty)
cv2.createTrackbar("saturation Min", "Trackbars",12,179,empty)
cv2.createTrackbar("saturation Max", "Trackbars",255,255,empty)
cv2.createTrackbar("value Min", "Trackbars",37,179,empty)
cv2.createTrackbar("value Max", "Trackbars",255,255,empty)

while True:

    imgresize = cv2.resize(img,(400,300))# resizing the image to make it smaller

    imghsv = cv2.cvtColor(imgresize,cv2.COLOR_BGR2HSV)# converts the image in hsv form

    #get position of trackbar
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")
    h_max = cv2.getTrackbarPos("Hue Max", "Trackbars")
    s_min = cv2.getTrackbarPos("saturation Min", "Trackbars")
    s_max = cv2.getTrackbarPos("saturation Max", "Trackbars")
    v_min = cv2.getTrackbarPos("value Min", "Trackbars")
    v_max = cv2.getTrackbarPos("value Max", "Trackbars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    #using track bar values
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imghsv,lower,upper)
    #Giving the masked image an actual result
    imgresult = cv2.bitwise_and(imgresize,imgresize,mask=mask)

    cv2.imshow('Resized image', imgresize)
    cv2.imshow('imghsv', imghsv)
    cv2.imshow('mask', mask)
    cv2.imshow('Result', imgresult)
    cv2.waitKey(1)