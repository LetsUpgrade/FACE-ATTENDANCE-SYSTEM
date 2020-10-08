# USAGE
# python gather_selfies.py --face-cascade cascades/haarcascade_frontalface_default.xml \
#	--output output/faces/adrian.txt

# import the necessary packages
from __future__ import print_function
#from facedetector import FaceDetector
#from imutils import encodings
#import argparse
#import imutils
#import cv2
#from __future__ import print_function
#from pyimagesearch.face_recognition import FaceRecognizer
from .facerecognizer import FaceRecognizer
from .facedetector import FaceDetector
from imutils import encodings
import numpy as np
import argparse
import imutils
import random
import glob
import cv2
import os

# construct the argument parse and parse command line arguments
#punit ap = argparse.ArgumentParser()
#punit ap.add_argument("-f", "--face-cascade", required=True, help="path to face detection cascade")
#punit ap.add_argument("-o", "--output", required=True, help="path to output file")
#punit ap.add_argument("-w", "--write-mode", type=str, default="a+", help="write method for the output file")
#punit args = vars(ap.parse_args())

# initialize the face detector, boolean indicating if we are in capturing mode or not, and
# the bounding box color
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.

def gather_selfies(employee_id):

	BasePath = Path(__file__).resolve(strict=True).parent
	#print(path)
	c_path = os.path.join('cascades','haarcascade_frontalface_default.xml') #newp)
	cascade_file = os.path.join(BasePath,c_path) #'cascades/haarcascade_frontalface_default.xml') #newp)

	#punit fd = FaceDetector(args["face_cascade"])
	fd = FaceDetector(cascade_file) #newp
	captureMode = False
	color = (0, 255, 0)

	# grab a reference to the webcam and open the output file for writing
	camera = cv2.VideoCapture(0)
	#punit f = open(args["output"], args["write_mode"])
	o_path = os.path.join('output','faces')  # newp
	output_path = os.path.join(BasePath,o_path) #'output/faces') #newp
	#output_path = os.path.join(BasePath,'output/faces')  # newp
	f = open(output_path+'/'+str(employee_id)+'.txt', "a+") #newp
	total = 0

	# loop over the frames of the video
	while True:
		# grab the current frame
		(grabbed, frame) = camera.read()

		# if the frame could not be grabbed, then we have reached the end of the video
		if not grabbed:
			print('reached end')
			break

		# resize the frame, convert the frame to grayscale, and detect faces in the frame
		frame = imutils.resize(frame, width=500)
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		faceRects = fd.detect(gray, scaleFactor=1.1, minNeighbors=9, minSize=(100, 100))

		# ensure that at least one face was detected
		if len(faceRects) > 0:
			# sort the bounding boxes, keeping only the largest one
			(x, y, w, h) = max(faceRects, key=lambda b:(b[2] * b[3]))

			# if we are in capture mode, extract the face ROI, encode it, and write it to file
			if captureMode:
				face = gray[y:y + h, x:x + w].copy(order="C")
				f.write("{}\n".format(encodings.base64_encode_image(face)))
				total += 1

			# draw bounding box on the frame
			cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

		# show the frame and record if the user presses a key
		cv2.imshow("Frame", frame)
		key = cv2.waitKey(1) & 0xFF

		# if the `c` key is pressed, then go into capture mode
		if key == ord("c"):
			# if we are not already in capture mode, drop into capture mode
			if not captureMode:
				captureMode = True
				color = (0, 0, 255)

			# otherwise, back out of capture mode
			else:
				captureMode = False
				color = (0, 255, 0)

		# if the `q` key is pressed, break from the loop
		elif key == ord("q"):
			break

	# close the output file, cleanup the camera, and close any open windows
	print("[INFO] wrote {} frames to file".format(total))
	f.close()
	camera.release()
	cv2.destroyAllWindows()

	#output_path = os.path.join(BasePath, 'output\\faces')  # newp
	#output_path = 'output/faces'  # newp
	c_path = os.path.join('output','classifier')  # newp
	classifier_path = os.path.join(BasePath, c_path) #'output/classifier')  # newp

	# initialize the face recognizer and the list of labels
	if imutils.is_cv2():
		fr = FaceRecognizer(cv2.createLBPHFaceRecognizer(radius=1, neighbors=8, grid_x=8, grid_y=8))

	else:
		fr = FaceRecognizer(cv2.face.LBPHFaceRecognizer_create(radius=1, neighbors=8, grid_x=8, grid_y=8))

	# initialize the list of labels
	labels = []

	# loop over the input faces for training
	for (i, path) in enumerate(glob.glob(output_path + "/*.txt")):
		# extract the person from the file name,
		name = path[path.rfind("/") + 1:].replace(".txt", "")
		print("[INFO] training on '{}'".format(name))

		# load the faces file, sample it, and initialize the list of faces
		sample = open(path).read().strip().split("\n")
		sample = random.sample(sample, min(len(sample), 200))
		faces = []

		# loop over the faces in the sample
		for face in sample:
			# decode the face and update the list of faces
			faces.append(encodings.base64_decode_image(face))

		# train the face detector on the faces and update the list of labels
		fr.train(faces, np.array([i] * len(faces)))
		labels.append(name)

	# update the face recognizer to include the face name labels, then write the model to file
	fr.setLabels(labels)
	fr.save(classifier_path)

	#file=os.path.isfile(output_path+'//'+str(employee_id)+'.txt')
	#return file

#gather_selfies('221629')