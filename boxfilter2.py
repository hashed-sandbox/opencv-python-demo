#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrate usage of filter2D() for image filtering.
"""

import numpy as np
import cv2

import sys
from utils import Timer

SIZE = 3
kernel = np.ones((SIZE, SIZE)) / (SIZE * SIZE)
     # = [[1/9, 1/9, 1/9],
     #    [1/9, 1/9, 1/9],  (SIZE = 3)
     #    [1/9, 1/9, 1/9]]

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    sys.exit("No cameras available!")

timer = Timer()
while True:
    ret, img_orig = cap.read()
    img_src = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)

    timer.start()

    img_dst = cv2.filter2D(img_src, -1, kernel)

    timer.end(img_dst)

    cv2.imshow("Before", img_src)
    cv2.imshow("After",  img_dst)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
