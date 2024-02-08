"""divakar ki aisi tesi"""
import cv2
import pytesseract
import numpy as np
import os
import tkinter as tk
from tkinter import *
from tkinter import filedialog
from roboflow import Roboflow
from login import image_path


name=image_path()



def bike_detection(image):

    rf = Roboflow(api_key="MW6fsjVoDPJTTqTzDOp6")
    project = rf.workspace().project("motorcycle-xjypd")
    model = project.version(1).model

    # infer on a local image
    print(model.predict(image, confidence=40, overlap=30).json())
    detected_bike=model.predict(image, confidence=40, overlap=30).json()
    return detected_bike
def helmet_detect(image):
    rf = Roboflow(api_key="MW6fsjVoDPJTTqTzDOp6")
    project = rf.workspace().project("bike-helmet-detection-2vdjo")
    model = project.version(1).model

    # infer on a local image
    print(model.predict(image, confidence=40, overlap=30).json())
    detected_helmet=model.predict(image, confidence=40, overlap=30).json()
    return detected_helmet



def bikeplate(img_name):
    global read
    img = cv2.imread(img_name)
    #CONVERTING COLOURED IMAGE INTO GREY
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nplate = cascade.detectMultiScale(gray,1.1,5)
    for (x,y,w,h) in nplate:
        #CROPING THE NUMBER PLATE FROM IMAGE
        a,b = (int(0.02*img.shape[0]),int(0.025*img.shape[1]))
        plate = img[y:y+h, x:x+w, :]
        cv2.imshow('plate',plate)
        #IMAGE PROCESSING USING OBJECT CHARACTER RECOGNITION(OCR)
        kernel = np.ones((1,1),np.uint8)
        plate = cv2.dilate(plate, kernel, iterations=1)
        plate = cv2.erode(plate, kernel, iterations=1)
        plate_gray= cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
        plate_blur = cv2.GaussianBlur(plate_gray, (5, 5), 0)
        plate = cv2.adaptiveThreshold(plate_blur, 253, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 157, 2.1)
        cv2.imshow('',plate)


        read= pytesseract.image_to_string(plate)
        number=read
        if(read[0:1]=="-"):
            state = read[2:4]
            number = read[2:13]
        else:
            state= read[2:4]
            
            
        try:
            print("The State from where car belongs to is:",States[state])
          
        except:
            print("State not recognised")
        return(read[2:13])
def carplate(img_name):
    global read
    img = cv2.imread(img_name)
    #CONVERTING COLOURED IMAGE INTO GREY
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    nplate = cascade.detectMultiScale(gray,1.9,5)
    
    for (x,y,w,h) in nplate:
        #CROPING THE NUMBER PLATE FROM IMAGE
        a,b = (int(0.02*img.shape[0]),int(0.026*img.shape[1]))
        plate = img[y+a:y+h-a, x+b:x+w-b, :]
        
        #IMAGE PROCESSING USING OBJECT CHARACTER RECOGNITION(OCR)
        kernel = np.ones((1,1),np.uint8)
        plate = cv2.dilate(plate, kernel, iterations=1)
        plate = cv2.erode(plate, kernel, iterations=1)
        plate_gray= cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
        plate_blur = cv2.GaussianBlur(plate_gray, (5, 5), 0)
        plate =cv2.adaptiveThreshold(plate_blur, 253, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 197, 2)
        read= pytesseract.image_to_string(plate)
        number=read
        if(read[0:1]==""):
            state = read[1:3]
            number = read[1:12]
        else:
            state= read[0:2]
            
        try:
            print("The State from where car belongs to is:",States[state])
          
        except:
            print("State not recognised")
        return(read[1:12])
        ##cv2.rectangle(img,(x,y-40),(x+w,y),(51,51,255),-1)
        #cv2.putText(img,read[1:12],(x,y-10),cv2.FONT_HERSHEY_COMPLEX,0.8,(222,55,89),2)
        #cv2.imshow('Plate',plate)
        
#SHOWING THE RESULT
    #cv2.imshow('Result',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()




if (__name__=="__name__"):

    
    pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    cascade = cv2.CascadeClassifier("haarcascade_russian_plate_number.xml")
    States={"AN":"Andaman and Nicobar","AP":"Andhra Pradesh","AR":"Arunachal Pradesh",
            "AS":"Assam","BR":"Bihar","CH":"Chandigarh","CG":"Chattisgarh"
            ,"DN":"Dadra and Nagar Haveli","DD":"Daman and Diu","DL":"Delhi"
            ,"GA":"Goa","GJ":"Gujarat","HR":"Haryana","HP":"Himachal Pradesh",
            "JK":"Jammu Kashmir","JH":"Jharkhand","KA":"Karnataka","KL":"Kerala",
            "LD":"Lakshadweep","MP":" Madhya Pradesh","MH":"Maharashtra",
            "MN":"Manipur","ML":"Meghalaya","MZ":"Mizoram","NL":"Nagaland",
            "OR":"Orissa","PY":"Pondicherry","PB":"Punjab","RJ":"Rajasthan",
            "SK":"Sikkim","TN":"Tamil Nadu","TR":"Tripura","UP":"Uttar Pradesh",
            "UK":"Uttrakhand","WB":"West Bengal"}
    image=bike_detection(name)
    if image['predictions'][0]['class']=='motorcycle':
        h=helmet_detect(name)
        number=bikeplate(name)
        if h['predictions'][0]['class']=='Without Helmet':
            print("helmet not detected")
    
    else:
        number=carplate(name)
        




