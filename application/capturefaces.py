#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import os
import imutils
from imutils import encodings
import numpy as np

class FaceDetector:
    def __init__(self, faceCascade):
        # load the face detector
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def detect(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):
       # detect faces in the image
        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE if imutils.is_cv2() else cv2.CASCADE_SCALE_IMAGE
        rects = faceCascade.detectMultiScale(image, scaleFactor=scaleFactor,
            minNeighbors=minNeighbors, minSize=minSize, flags=flags)

       # return the bounding boxes around the faces in the image
        return rects

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height
employeeID=input("Enter your ID:")
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count
count = 0
while(True):
    ret, image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faceRects = FaceDetector# calling class to detect faces
    faceRects = faceRects.detect(gray, scaleFactor=1.1, minNeighbors=9, minSize=(100, 100))
    filename="output/captured_faces/"+employeeID+".txt"    
    count=0    
    # ensure that at least one face was detected
    if len(faceRects) > 0:
    # sort the bounding boxes, keeping only the largest one
        (x, y, w, h) = max(faceRects, key=lambda b:(b[2] * b[3]))
        face = gray[y:y + h, x:x + w].copy(order="C")
        f=open(filename,"w")
        f.write("{}\n".format(encodings.base64_encode_image(face))) # encoding the detected face to base64 string and storing it in a text file
        count+=1
    cv2.imshow('image', face)
    k = cv2.waitKey(2000) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 1: # Take 1 face sample and stop video
         break
            
# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()


# In[ ]:




