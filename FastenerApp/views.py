import matplotlib
matplotlib.use('Agg')
from django.shortcuts import render
from django.template import RequestContext
from django.contrib import messages
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import os
import base64
import numpy as np
import io
import matplotlib.pyplot as plt
import cv2
from ultralytics import YOLO

global username, yolo_model

#yolo confidence threshold to detect animal species
CONFIDENCE_THRESHOLD = 0.30
GREEN = (0, 255, 0)

yolo_model = YOLO("model/best.pt")
print("Yolo Model Loaded")

def detectFastener(frame):
    global yolo_model
    labels =  ['Allen Bolt', 'Blind-Pop Rivet', 'Cap Nut', 'Coupling Nut', 'Drywall Anchor', 'Dyna Bolt', 'Eye Bolt', 'Flange Bolt', 'Flange Nut',
               'Flat Washer', 'Hanger Bolt',  'Hex Bolt', 'Hex Head Anchor', 'Hex Nut', 'Lag Screw Bolt', 'Lock Nut', 'Lock Washers-Split Washer',
               'Mechanical Expansion Anchor','Nails', 'Screw Hook', 'Snap-Head Rivet', 'Square Nut', 'Stud Bolt', 'Threaded Rivet', 'U Bolt', 'Wing Nut']
    detections = yolo_model(frame)[0]
    # loop over the detections
    for data in detections.boxes.data.tolist():
        print(data)
        # extract the confidence (i.e., probability) associated with the detection
        confidence = data[4]
        cls_id = data[5]
        # filter out weak detections by ensuring the 
        # confidence is greater than the minimum confidence
        if float(confidence) >= CONFIDENCE_THRESHOLD:
            xmin, ymin, xmax, ymax = int(data[0]), int(data[1]), int(data[2]), int(data[3])
            cv2.rectangle(frame, (xmin, ymin) , (xmax, ymax), GREEN, 2)
            cv2.putText(frame, labels[int(cls_id)]+" "+str(round(confidence,2)), (xmin, ymin+20),  cv2.FONT_HERSHEY_SIMPLEX,0.7, (255, 0, 0), 2)               
    return frame    

def FastenerDetectionAction(request):
    if request.method == 'POST':
        filename = request.FILES['t1'].name
        image = request.FILES['t1'].read() #reading uploaded file from user
        if os.path.exists("FastenerApp/static/"+filename):
            os.remove("FastenerApp/static/"+filename)
        with open("FastenerApp/static/"+filename, "wb") as file:
            file.write(image)
        file.close()
        img = cv2.imread("FastenerApp/static/"+filename)
        #img = cv2.resize(img, (640, 640))
        img = detectFastener(img)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        #img = cv2.resize(img, (600,300))#display image with predicted output
        plt.imshow(img)
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        img_b64 = base64.b64encode(buf.getvalue()).decode()
        #plt.clf()
        #plt.cla()
        #plt.close()
        context= {'data':"Fastener Detected Output", 'img': img_b64}
        return render(request, 'index.html', context)

def FastenerDetection(request):
    if request.method == 'GET':
        return render(request,'FastenerDetection.html', {})     

def index(request):
    if request.method == 'GET':
        return render(request,'index.html', {})


        


        
