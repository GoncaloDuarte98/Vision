# import the necessary packages
import argparse
from pyimagesearch.shapedetector import ShapeDetector
import argparse
import imutils
import numpy as np
import cv2

# load the image and resize it
image = cv2.imread('image_0.jpg', 1)
resized = imutils.resize(image, height=1000)
ratio = image.shape[0] / float(resized.shape[0])
image = resized.copy()
original = image.copy()
#image = cv2.add(original, np.array([20.0]))
image = cv2.medianBlur(image, 7)
#image = cv2.bilateralFilter(image,9,75,75)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Search individual colors (flavours) and create masks

# background mask

bg_mask = cv2.inRange(hsv, (0, 115, 0), (180, 255, 255))
bg_mask = cv2.bitwise_and(hsv, hsv, mask=bg_mask)
bg_mask = cv2.cvtColor(bg_mask, cv2.COLOR_HSV2BGR)

cv2.imshow("COUNTOURS", bg_mask)
cv2.waitKey()


# red mask
red_mask = cv2.inRange(hsv, (0, 100, 20), (3, 255, 255))
red_mask = cv2.bitwise_and(hsv, hsv, mask=red_mask)
red_mask = cv2.cvtColor(red_mask, cv2.COLOR_HSV2BGR)

# dark red mask
dark_red_mask = cv2.inRange(hsv, (170, 100, 20), (180, 255, 255))
dark_red_mask = cv2.bitwise_and(hsv, hsv, mask=dark_red_mask)
dark_red_mask = cv2.cvtColor(dark_red_mask, cv2.COLOR_HSV2BGR)

# orange mask
orange_mask = cv2.inRange(hsv, (10, 100, 20), (20, 255, 255))
orange_mask = cv2.bitwise_and(hsv, hsv, mask=orange_mask)
orange_mask = cv2.cvtColor(orange_mask, cv2.COLOR_HSV2BGR)

# green mask
green_mask = cv2.inRange(hsv, (35, 52, 72), (102, 255, 255))
green_mask = cv2.bitwise_and(hsv, hsv, mask=green_mask)
green_mask = cv2.cvtColor(green_mask, cv2.COLOR_HSV2BGR)

# yellow mask
yellow_mask = cv2.inRange(hsv, (20, 100, 100), (30, 255, 255))
yellow_mask = cv2.bitwise_and(hsv, hsv, mask=yellow_mask)
yellow_mask = cv2.cvtColor(yellow_mask, cv2.COLOR_HSV2BGR)

# white/tan mask

white_mask = cv2.inRange(hsv, ((46 / 2) - 10, (33 * 2.55) - 10, (69 * 2.55) - 20),
                         ((46 / 2) + 20, (33 * 2.55) + 20, (69 * 2.55) + 20))
white_mask = cv2.bitwise_and(hsv, hsv, mask=white_mask)
white_mask = cv2.cvtColor(white_mask, cv2.COLOR_HSV2BGR)


# function to identify the candy
def shape_identifier(mask):
    cv2.imshow("mask",mask)
    cv2.waitKey()
    r_mask = cv2.medianBlur(mask, 23)
    gray = cv2.cvtColor(r_mask, cv2.COLOR_BGR2GRAY)
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 9, 10)

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    cv2.imshow("thresh", thresh)
    cv2.waitKey()

    #comeca aqui
    for c in cnts:
        ellipse = cv2.fitEllipse(c)
        (center, axes, orientation) = ellipse
        majoraxis_length = max(axes)
        minoraxis_length = min(axes)
        eccentricity = (np.sqrt(1 - (minoraxis_length / majoraxis_length) ** 2))
        if eccentricity < 0.7:
            cv2.ellipse(original, ellipse, (0, 0, 255), 2)
        else:
            cv2.drawContours(original, [c], -1, (0, 255, 0), 2)

        #cv2.imshow("COUNTOURS", mask)
        print(eccentricity)
        #cv2.waitKey()


    #cv2.imshow("COUNTOURS", mask)
    #cv2.waitKey()



    """
    #cv2.imshow("mask", thresh)
    # cv2.imshow("thrsh", original)
    #cv2.waitKey()

    # find are of minimum ratio (worm) and its height
    min_ratio = 999;
    area_min_ratio = 0
    height_min_ratio = 0


    for c in cnts:
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # check area and aspect ratio
        peri = cv2.arcLength(box, True)
        area = cv2.contourArea(box)
        (x, y), (width, height), angle = cv2.minAreaRect(c)
        aspect_ratio = min(width, height) / max(width, height)
        aspect_ratio = round(aspect_ratio, 2)

        if aspect_ratio < min_ratio:
            min_ratio = aspect_ratio
            area_min_ratio = area
            if height>width:
                height_min_ratio=height
            else:
                height_min_ratio=width

    # check relative area


    for c in cnts:
        # convert to box

        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)

        # check area
        peri = cv2.arcLength(box, True)
        area = cv2.contourArea(box)
        (x, y), (width, height), angle = cv2.minAreaRect(c)
        aspect_ratio = min(width, height) / max(width, height)
        aspect_ratio = round(aspect_ratio, 2)
        aspect_ratio = str(aspect_ratio)
        #relative_area = round(area_min_ratio / area, 2)
        if height > width:
            altura=height
            relative_height=round(height/height_min_ratio,2)
        else:
            altura = width
            relative_height=round(width/height_min_ratio,2)


        if area > 100:
            # minhoca
            cv2.drawContours(original, [box], -1, (0, 0, 255), 1)
            cv2.putText(original, str(round(altura,2)), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)
            print("perimetro:", peri, "area: ", area, "  vertices:", len(c))

            # (x, y), (width, height), angle = rect
            # aspect_ratio = min(w, h) / max(w, h)

            # cv2.putText(original, str(round(aspect_ratio,2)), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)

            # cv2.drawContours(original, [box], 0, (0, 0, 255), 2)

            # cv2.imshow("imagem", original)
            # cv2.waitKey()
    """


shape_identifier(red_mask)
shape_identifier(dark_red_mask)
shape_identifier(green_mask)
shape_identifier(orange_mask)
shape_identifier(yellow_mask)
#shape_identifier(white_mask)

cv2.imshow("imagem", original)
# cv2.imshow("mask", )
cv2.waitKey()
