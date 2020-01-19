# import the necessary packages
import argparse
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import numpy as np
import cv2
from matplotlib import pyplot as plt

# load the image and resize it to a smaller factor so that the shapes can be approximated better
image = cv2.imread('image.jpg', 1)
resized = imutils.resize(image, width=1000)
ratio = image.shape[0] / float(resized.shape[0])
image = resized.copy()

#TESTE--------------------------------------------------------------------------------------------------------------------------

#TESTE--------------------------------------------------------------------------------------------------------------------------



# threshold the image

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (7, 7), 0)
thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

thresh = cv2.GaussianBlur(thresh, (9, 9), 0)
thresh = cv2.adaptiveThreshold(thresh, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

thresh = cv2.GaussianBlur(thresh, (3, 3), 0)
thresh = cv2.erode(thresh,(5,5),iterations = 5)







# find contours in the threshold image
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,  cv2.CHAIN_APPROX_TC89_KCOS)
cnts = imutils.grab_contours(cnts)

# loop over the contours
for c in cnts:
    # draw the contour on the image



    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    area = cv2.contourArea(c)


    print("perimetro:",peri,"area: ",area,"  vertices:",len(approx))



    #cv2.imshow("th3", image)
    #cv2.waitKey()




cv2.imshow("th3", image)
cv2.waitKey()







