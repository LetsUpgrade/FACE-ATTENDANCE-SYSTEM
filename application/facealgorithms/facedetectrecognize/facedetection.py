#!/usr/bin/env python
# coding: utf-8

# In[10]:


import cv2

class FaceDetector:
    def __init__(self, faceCascade):
        # load the face detector
        self.faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def detect(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):
        faceCascade=cv2.CascadeClassifier("C:\\Users\\DELL\\AppData\\Roaming\\Python\\Python37\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")
        # detect faces in the image
        flags = cv2.cv.CV_HAAR_SCALE_IMAGE if imutils.is_cv2() else cv2.CASCADE_SCALE_IMAGE
        rects = faceCascade.detectMultiScale(image, scaleFactor=scaleFactor,
            minNeighbors=minNeighbors, minSize=minSize, flags=flags)

       # return the bounding boxes around the faces in the image
        return rects

