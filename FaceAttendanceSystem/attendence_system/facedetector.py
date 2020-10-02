# import the necessary packages
import cv2
import imutils

class FaceDetector:
	def __init__(self, faceCascadePath):
		# load the face detector
		self.faceCascade = cv2.CascadeClassifier(faceCascadePath)

	def detect(self, image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)):
		# detect faces in the image
		flags = cv2.cv.CV_HAAR_SCALE_IMAGE if imutils.is_cv2() else cv2.CASCADE_SCALE_IMAGE
		rects = self.faceCascade.detectMultiScale(image, scaleFactor=scaleFactor,
			minNeighbors=minNeighbors, minSize=minSize, flags=flags)

		# return the bounding boxes around the faces in the image
		return rects
