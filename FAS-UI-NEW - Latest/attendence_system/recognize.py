# USAGE
# python recognize.py --face-cascade cascades/haarcascade_frontalface_default.xml --classifier output/classifier

# import the necessary packages
#from pyimagesearch.face_recognition import FaceDetector
#from pyimagesearch.face_recognition import FaceRecognizer
from .facedetector import FaceDetector
from .facerecognizer import FaceRecognizer
import argparse
import imutils
import cv2
from pathlib import Path
import os

def recognize():
	# construct the argument parse and parse command line arguments
	#ap = argparse.ArgumentParser()
	#ap.add_argument("-f", "--face-cascade", required=True, help="path to face detection cascade")
	#ap.add_argument("-c", "--classifier", required=True, help="path to the classifier")
	#ap.add_argument("-t", "--confidence", type=float, default=100.0,
	#	help="maximum confidence threshold for positive face identification")
	#args = vars(ap.parse_args())

	#def recognize():
	# output_path = os.path.join(BasePath, 'output\\faces')  # newp
	# output_path = 'output/faces'  # newp
	BasePath = Path(__file__).resolve(strict=True).parent
	c_path = os.path.join('output','classifier')
	classifier_path = os.path.join(BasePath, c_path)  # newp
	# print(path)

	c_path = os.path.join('cascades', 'haarcascade_frontalface_default.xml')  # newp)
	cascade_file = os.path.join(BasePath, c_path)  # 'cascades/haarcascade_frontalface_default.xml') #newp)

	#cascade_file = os.path.join(BasePath, 'cascades/haarcascade_frontalface_default.xml')  # newp)
	#cascade_file = 'cascades/haarcascade_frontalface_default.xml' #newp
	#classifier_path= 'output/classifier' #newp
	# initialize the face detector, load the face recognizer, and set the confidence
	# threshold
	fd = FaceDetector(cascade_file)
	fr = FaceRecognizer.load(classifier_path)
	fr.setConfidenceThreshold(confidenceThreshold=100)

	# grab a reference to the webcam
	camera = cv2.VideoCapture(0)

	# loop over the frames of the video
	while True:
		# grab the current frame
		(grabbed, frame) = camera.read()

		# if the frame could not be grabbed, then we have reached the end of the video
		if not grabbed:
			break

		# resize the frame, convert the frame to grayscale, and detect faces in the frame
		frame = imutils.resize(frame, width=500)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

		# loop over the face bounding boxes
		for (i, (x, y, w, h)) in enumerate(faceRects):
			# grab the face to predict
			face = gray[y:y + h, x:x + w]

			# predict who's face it is, display the text on the image, and draw a bounding
			# box around the face
			(prediction, confidence) = fr.predict(face)
			prediction1 = "{}: {:.2f}".format(prediction, confidence)
			cv2.putText(frame, prediction1, (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.25, (0, 255, 0), 2)
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

		# show the frame and record if the user presses a key
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `q` key is pressed, break from the loop
		if key == ord("q"):
			break

	# cleanup the camera and close any open windows
	camera.release()
	cv2.destroyAllWindows()

	return prediction