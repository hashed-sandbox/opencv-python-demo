#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrate basic techniques of face detection.
"""

import numpy as np
import cv2

import sys

CASCADE_NAME = "C:\opencv\sources\data\haarcascades\haarcascade_frontalface_alt2.xml"
cascade = cv2.CascadeClassifier(CASCADE_NAME)

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    sys.exit("No cameras available!")

while True:
    ret, img_cap = cap.read()

    faces = cascade.detectMultiScale(img_cap, scaleFactor=1.2,
                                     minNeighbors=4, minSize=(30, 30),
                                     flags=cv2.CASCADE_SCALE_IMAGE)
    if len(faces) > 0:
        faces[:,2:] += faces[:,:2]

    for x1, y1, x2, y2 in faces:
        cv2.rectangle(img_cap, (x1, y1), (x2, y2), (0, 255, 255), 1)

    cv2.imshow("Face Detection", img_cap)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
