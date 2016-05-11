#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrate basic techniques of background subtraction method.
"""

import numpy as np
import cv2

import sys

ALPHA = 0.1
THRESHOLD = 30

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    sys.exit("No cameras available!")

# initialize a image (acc) to store running averages

ret, img_orig = cap.read()
img_fg = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)

acc = np.empty(img_fg.shape, dtype=np.float32)
cv2.accumulateWeighted(img_fg, acc, 1.0)

while True:
    ret, img_orig = cap.read()
    img_fg = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)

    img_bg = acc.astype(np.uint8)  # copy and cast from float32 to uint8
    cv2.imshow("Background", img_bg)

    cv2.accumulateWeighted(img_fg, acc, ALPHA)

    img_bg = cv2.absdiff(img_fg, img_bg)
    ret, img_bg = cv2.threshold(img_bg, THRESHOLD, 255, cv2.THRESH_BINARY)

    kernel = np.ones(img_bg.shape, dtype=np.uint8)
    img_bg = cv2.dilate(img_bg, kernel, iterations=1)
    img_bg = cv2.erode(img_bg, kernel, iterations=1)

    img_fg = cv2.bitwise_and(img_fg, img_bg)
    cv2.imshow("Foreground", img_fg)

    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()



