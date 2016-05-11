#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
An example of applications of affine transformations.
"""

import numpy as np
import cv2

def mirror4(img):
    """
    Create 4 mirrored images and return a merged one.

    img: a gray-scaled image
    """
    height, width = img.shape

    # the upper left
    affine = np.array([[0.5, 0.0, 0.0],
                       [0.0, 0.5, 0.0]])
    img_tmp1 = cv2.warpAffine(img, affine, (width, height))

    # the upper right
    affine = np.array([[-0.5, 0.0, width-1],
                       [ 0.0, 0.5,     0.0]])
    img_tmp2 = cv2.warpAffine(img, affine, (width, height))

    # the lower right
    affine = np.array([[-0.5,  0.0,  width-1],
                       [ 0.0, -0.5, height-1]])
    img_tmp3 = cv2.warpAffine(img, affine, (width, height))

    # the lower left
    affine = np.array([[0.5,  0.0,      0.0],
                       [0.0, -0.5, height-1]])
    img_tmp4 = cv2.warpAffine(img, affine, (width, height))

    return cv2.add(cv2.add(img_tmp1, img_tmp2), cv2.add(img_tmp3, img_tmp4))

if __name__ == "__main__":
    import sys

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        sys.exit("No cameras available!")

    while True:
        ret, img_orig = cap.read()
        img_src = cv2.cvtColor(img_orig, cv2.COLOR_BGR2GRAY)

        img_dst = mirror4(img_src)

        cv2.imshow("Before", img_src)
        cv2.imshow("After",  img_dst)

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

    cv2.destroyAllWindows()
