import cv2
import numpy as np

#Functions to get contours from the images
def getcontours(img):
    #checks only the external edges...
    contours,heirachy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)#gives the area
        print(area)
        if area > 200:
            cv2.drawContours(imgcontour,cnt,-1,(255,0,0),3)
            perimeter = cv2.arcLength(cnt,True)
            print(perimeter)
            #Approximate corner points
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter,True)
            print(len(approx))
            objcorner = len(approx)
            #Creating a box that bounds the shape
            x,y,w,h = cv2.boundingRect(approx)

            #Checks condition to decide the shape
            if objcorner ==3: objectType = "Tri"
            elif objcorner == 4:
                aspectratio = w/ float(h)
                if aspectratio > 0.95 and aspectratio<1.05: objectType = "Square"
                else:objectType = "rectangle"
            elif objcorner > 4: objectType = "circle"
            else: objectType ="none"
            cv2.rectangle(imgcontour,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(imgcontour,objectType,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,0,0),2)

img = cv2.imread('shape.jpg')
imgcontour = img.copy()

#convert to greyscale
imggray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgblur = cv2.GaussianBlur(imggray,(7,7),1)
imgcanny = cv2.Canny(imgblur,50,50)
getcontours(imgcanny)#Calling the function

cv2.imshow('Original',img)
cv2.imshow('Grey',imggray)
cv2.imshow('Blurred',imgblur)
cv2.imshow('Canny',imgcanny)
cv2.imshow('Contour',imgcontour)
cv2.waitKey(0)