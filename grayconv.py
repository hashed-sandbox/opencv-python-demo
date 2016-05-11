#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrate basic techniques of image thresholding.
"""

import numpy as np
import cv2

import random
import sys

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    sys.exit("No cameras available!")

while True:
    ret, img_orig = cap.read()
    img_src = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)

    img_dst = np.empty_like(img_src)
    height, width = img_dst.shape  # numpy.ndarray.shape

    for y in xrange(height):
        for x in xrange(width):
            val = img_src[y][x]
            if val < random.randrange(256):
                img_dst[y][x] = 0
            else:
                img_dst[y][x] = 255

    cv2.imshow("Before", img_src)
    cv2.imshow("After",  img_dst)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()
