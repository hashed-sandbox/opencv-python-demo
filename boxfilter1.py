#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Demonstrate a basic concept of image filtering.
"""

import numpy as np
import cv2

def boxfilter(img, size, x, y):
    """
    Calculate a box-filtered value for a given point.

    img: a gray-scaled image
    size: the size of a box filter
    x, y: coordinates
    """

    height, width = img.shape  # numpy.ndarray.shape
    values = []

    for i in xrange(size):
        py = y + i - (size / 2)
        if py < 0:
            py = 0
        elif py > height - 1:
            py = height - 1

        for j in xrange(size):
            px = x + j - (size / 2)
            if px < 0:
                px = 0
            elif px > width - 1:
                px = width - 1

            values.append(img[py][px])

    return int(round(sum(values) / len(values)))

if __name__ == "__main__":
    import sys
    from utils import Timer

    SIZE = 3

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        sys.exit("No cameras available!")

    timer = Timer()
    while True:
        ret, img_orig = cap.read()
        img_src = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)

        img_dst = np.empty_like(img_src)
        height, width = img_dst.shape  # numpy.ndarray.shape

        timer.start()

        for y in xrange(height):
            for x in xrange(width):
                img_dst[y][x] = boxfilter(img_src, SIZE, x, y)

        timer.end(img_dst)

        cv2.imshow("Before", img_src)
        cv2.imshow("After",  img_dst)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()
