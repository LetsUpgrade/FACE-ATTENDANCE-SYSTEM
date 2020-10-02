# FACE ATTENDANCE SYSTEM
![](/img/FASlogo.png)
![FAS](https://github.com/Gaya3priya/face_attendance/blob/master/img/FASlogo.jpg)
## Description:
An face detector developed to mark the attendance of a student which is developed with the help of computer vision and deep learning using Python, OpenCV, and TensorFlow/Keras. In the present scenario due to Covid-19, there is no efficient education systems other than the online facilities, attendence has become an issue. This app can help in taking the attendence not only in educational institutions, but also in the offices.


## Prerequisites:
All the dependencies and required libraries are included in the file [requirements.txt](requirements.txt)

## Installation:
1. clone the repo
```
$ git clone https://github.com/Gaya3priya/face_attendance.git
```
2.Change your directory to the cloned repo and create a Python virtual environment named 'testenv'
```
$ mkvirtualenv testenv
```
3.Now, run the following command in your Terminal/Command Prompt to install the libraries required
```
$ pip3 install -r requirements.txt
```


## Objectives of the project:
#### 1) Gathering Selfies.
#### 2) Detection.
#### 3) Recognition.

### - Gathering Selfies:

System will capture image of the user through webcam.Once face of the user is shown up in webcam, then we will detect the face in the webcam by using haarcascade_frontalface_default.xml.Once face is detected we will capture each frame of user face in different scale and angle like which is in the [gather_selfies.py](https://github.com/Gaya3priya/face_attendance/blob/master/capturefaces.py) file.
These frames will be encoded in text format and saving them with employeeID.txt by asking user/employee to enter his/her ID and will be saved in [output/faces](https://github.com/Gaya3priya/face_attendance/tree/master/output/captured_faces) folder in our system for future use.

### - Detection:

The [facedetector.py](https://github.com/Gaya3priya/face_attendance/blob/master/facealgorithms/facedetectrecognize/facedetection.py) file will detect faces in the image by using haarcascade_frontalface_default.xml and OpenCV.And return the bounding boxes around the faces in the image.The [facedetector.py](https://github.com/Gaya3priya/face_attendance/blob/master/facealgorithms/facedetectrecognize/facedetector.py) file will be like liveness detection.It can detect faces without detecting fake faces.

### - Recognition:

Recognition is done by LBPH recogniser.
Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.
LBPH is one of the easiest face recognition algorithms. It can represent local features in the images. It is possible to get great results (mainly in a controlled environment). It is robust against monotonic gray scale transformations. It is provided by the OpenCV library (Open Source Computer Vision Library).
The [facerecognizer.py] file will be used to recognize the faces

## Python libraries used:
#### - OpenCV-python
#### - Numpy
#### - Pillow
#### - imutils
#### - glob
