# -*- coding: utf-8 -*-

import cv2

class Timer:
    """
    Measure and print the elapsed time between start() and end().
    """

    def __init__(self):
        pass

    def start(self):
        """
        Start to measure the time.
        """

        self.tickStart = cv2.getTickCount()

    def end(self, img_out):
        """
        Stop measuring and print the duration on img_out.

        img_out: a gray-scaled image
        """

        dt = (cv2.getTickCount() - self.tickStart) / cv2.getTickFrequency()
        dt *= 1000  #[msec/frame]

        height, width = img_out.shape  # numpy.ndarray.shape
        cv2.putText(img_out, "{:.1f} msec/frame".format(dt),
                    (width / 10, height / 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, 255)
