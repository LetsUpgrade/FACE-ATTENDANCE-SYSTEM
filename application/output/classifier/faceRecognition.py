import cv2
import numpy as np

faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam=cv2.VideoCapture(0);
rec=cv2.createLBPHFaceRecognizer();
rec.load("recognizer/trainningData.yml")
id=0
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,5,1,0,4)
while(True):
	ret,img=cam.read();
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	faces=faceDetect.detectMultiScale(gray,1.3,5);
	for(x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
		id,conf=rec.predict(gray[y:y+h,x:x+w])
		cv2.cv.PutText(cv2.cv.fromarray(img),str(id),(x,y+h),font,255);
	cv2.imshow("Face",img);
	if(cv2.waitKey(1)==ord('q')):
		break;
cam.release()
cv2.destroyAllWindows()
