#!/usr/bin/env python
# coding: utf-8

# In[3]:


import cv2
import numpy
import glob
from PIL import Image as PImage
def load_images_from_folders(folders=glob.glob('E:\\MY PROJECT\\caltech_faces\\*')):
    folders = glob.glob('E:\\MY PROJECT\\caltech_faces\\*')
    imagenames_list = []
    for folder in folders:
        for img in glob.glob(folder+'/*.jpg'):
            img = PImage.open(img)
            imagenames_list.append(img)
    return imagenames_list    
imagenames_list=load_images_from_folders()
imagenames_list[2].show()

#Glob allows you to query files like you would in a terminal. 
#Once you have Glob you could save all of the file names to a list and 
#then loop through this list reading your images (NumPy arrays) into a new list.

