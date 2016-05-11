#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Imitate effects of tilt-shift lense.
"""

import numpy as np
import cv2

import sys
from boxfilter1 import boxfilter

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    sys.exit("No cameras available!")

while True:
    ret, img_orig = cap.read()
    img_src = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)

    img_dst = np.empty_like(img_src)
    height, width = img_dst.shape

    for y in xrange(height):
        size = abs(height * 0.8 - y) * 20 / height + 1

        for x in xrange(width):
            img_dst[y][x] =  boxfilter(img_src, int(size), x, y)

    cv2.imshow("Before", img_src)
    cv2.imshow("After",  img_dst)

    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

