# Face Attendance System Workflow
Our aim is to create a face attendance system.
It will also serve purpose of entry of authorized users in the premise of organization.

## We can have 3 scenarios
1. New users
2. Existing users
3. Unknown users

### 1. New users: 

   When our system will register new user information, then we will train the face of new user so that our system will recognize the 
   face of the user next time when s/he register her/his attendance.

To achieve this, 

a. System will capture new users face through webcam.
b. Once users face is shown up in webcam, then we will detect user face in the webcam.
c. Once face is detected we will capture each frame of user faces in different scale and angle.
d. These frames will be encoded in text format and will be saved in our system for future use.
d. Then we will perform training to recognize this new face onto our system and this pretrained model will be stored in our system for future face recognition task.

### 2. Existing Users:

   When existing users come in, then s/he would register her/his attendance or would try to enter the premise of organization..
   
To achieve this,

a. System will capture user face through webcam.
b. Once users face is shown up in webcam, then pretrained model will be loaded and applied on the face to recognize the face.
c. System will recognize the face based on confidence level of the prediction.

### 3. Unknown Users:

   When any person comes in, then s/he would try to register her/his attendance or would try to enter the premise of organization.
   If our pretrained model doesn't recognize the face then it would not register her/his attendance and system would recognize as Unknown user.

## Source Code Writing Approach:
We will follow modular approach to develop our source codes.
 
## Sample Source code and Standard:
Please follow below coding standard conventions.
### Sample Code:
import cv2

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

### Coding Standard:
1.	 Imports should usually be on separate lines
2.	Avoid trailing whitespace anywhere. Because it's usually invisible, it can be confusing.
3.	Compound statements (multiple statements on the same line) are generally discouraged
4.	Comments should be complete sentences. Always make a priority of keeping the comments up-to-date when the code changes. Ensure that your comments are clear and easily understandable to other speakers of the language you are writing in.
5.	Never use the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase letter eye) as single character variable names.
6.	The name of the variables should start with small case capital letters and a multi word variable should be named as: word1_word2_word3.
7.	The variable name should be appropriate based on the things that they do. DO NOT USE NAMES LIKE x, k, y etc.  Always use a meaningful English word. For example, faceCascade
8.	Method names should start with small case characters. They should start with a verb and make a meaningful sense of what they are supposed to accomplish. For e.g.: detect()
9.	Always use self for the first argument to instance methods.
10.	Class names should normally use the CapWords convention. Class name should also represent the functionality of the class. For e.g. FaceDetector ()
11.	Modules/Packages/Folders should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. For e.g.: facedetectrecognize, facedetection.py etc
12.	Comparisons to singletons like None should always be done with is or is not, never the equality operators
13.	Be consistent in return statements. Either all return statements in a function should return an expression, or none of them should. If any return statement returns an expression, any return statements where no value is returned should explicitly state this as return None, and an explicit return statement should be present at the end of the function (if reachable)
