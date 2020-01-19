# import the necessary packages
import argparse
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import numpy as np
import cv2

# load the image and resize it
image = cv2.imread('image_2.jpg', 1)
original = image
resized = imutils.resize(image, height=1000)
ratio = image.shape[0] / float(resized.shape[0])
image = resized.copy()

image = cv2.medianBlur(image, 11)

src = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow("orginal", src)

cv2.waitKey()



hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Search individual colors (flavours) and create masks

# background mask

bg_mask = cv2.inRange(hsv, (0, 115, 0), (180, 255, 255))
bg_mask = cv2.bitwise_and(hsv, hsv, mask=bg_mask)
bg_mask = cv2.cvtColor(bg_mask, cv2.COLOR_HSV2BGR)

bg_mask = cv2.cvtColor(bg_mask, cv2.COLOR_BGR2GRAY)

cv2.imshow("COUNTOURS", bg_mask)
cv2.waitKey()





circles = cv2.HoughCircles(bg_mask, cv2.HOUGH_GRADIENT, 1, 100, param1=190, param2=40, minRadius=0, maxRadius=99)
circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    # draw the outer circle
    cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), -1)

cv2.imshow("orginal", image)

cv2.waitKey()
