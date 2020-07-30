import cv2
import numpy as np
import os

cap=cv2.VideoCapture(0)
detector=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
i=1
while True:
    
    red, frame=cap.read()
    gray=None
    if red:
        faces=detector.detectMultiScale(frame)

        for face in faces:
            x,y,w,h=face
            cut=frame[y:y+h,x:x+w]
            fix=cv2.resize(cut,(200,200))
            gray=cv2.cvtColor(fix,cv2.COLOR_BGR2GRAY)
            cv2.imshow("Frame",gray)
            _dir="D:\\30DaysML\\fifthday\dataset"
            _dir=os.path.join(_dir,"manoj")
            if not os.path.exists(_dir):
                os.makedirs(_dir)   
            if cv2.waitKey(20)==ord("s") :
                cv2.imwrite(os.path.join(_dir,str(i)+".jpg"),gray)
                i=i+1
        cv2.imshow("Frame",frame)
       # name="manoj"
        #_dir="D:\\30DaysML\\fifthday\dataset"
        #_dir=os.path.join(_dir,name)
        #if not os.path.exists(_dir):
         #   os.makedirs(_dir)   
        if cv2.waitKey(20)==ord("q") :
           # cv2.imwrite(os.path.join(_dir,i+".jpg"),gray)
           break

cap.release()
cv2.destroyAllWindows()