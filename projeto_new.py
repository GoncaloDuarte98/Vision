import imutils
import numpy as np
import cv2


def mask_process(mask):
    gray = mask.copy()
    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 7)

    cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    '''
    for c in cnts:
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        area = cv2.contourArea(box)
        (x, y), (width, height), angle = cv2.minAreaRect(c)
        biggest_size = max(width, height)

        if area > 2500 or biggest_size > 70:
            cv2.drawContours(image, [box], 0, (0, 255, 0), 2)
        elif area>800:
            cv2.drawContours(image, [box], 0, (0, 0, 255), 2)

    '''
    cv2.imshow("MASK", thresh)
    cv2.imshow("red MASK", mask)
    cv2.waitKey()


def color_separation(image):
    img=cv2.bilateralFilter(image,9,75,75)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    kernel = np.ones((15,15), np.uint8)

    # red mask
    red_mask = cv2.inRange(hsv, np.array([0, 100, 20]), np.array([3, 255, 255]))
    red_mask= cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)


    # red_mask = cv2.bitwise_and(hsv, hsv, mask=red_mask)
    #red_mask = cv2.cvtColor(red_mask, cv2.COLOR_HSV2BGR)

    mask_process(red_mask)



def mask_select(image):
    img = imutils.resize(image, height=700)
    img = cv2.medianBlur(img, 7)
    # img = cv2.bilateralFilter(img, 9, 99, 99)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # red mask
    bg_mask = cv2.inRange(hsv, (0, 100, 20), (5, 255, 255))
    bg_mask = cv2.bitwise_and(hsv, hsv, mask=bg_mask)
    bg_mask = cv2.cvtColor(bg_mask, cv2.COLOR_HSV2BGR)

    color_separation(bg_mask)

    # cv2.imshow("COUNTOURS", img)
    # cv2.imshow("mask", bg_mask)
    # cv2.waitKey()


def Remove_Background(image):
    img = image.copy()
    img =
    img = cv2.bilateralFilter(img, 9, 75, 75)


    # bi = cv2.GaussianBlur(img,(5,5),0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Background mask
    bg_mask = cv2.inRange(hsv, (0, 100, 20), (255, 255, 255))
    bg_mask = cv2.bitwise_and(hsv, hsv, mask=bg_mask)
    bg_mask = cv2.cvtColor(bg_mask, cv2.COLOR_HSV2BGR)
    #bg_mask = cv2.GaussianBlur(bg_mask,(5,5),0)


    cv2.imshow("red MASK", bg_mask)
    cv2.waitKey()


    #color_separation(bg_mask)






def main():
    print("hello world")
    for x in range(46):
        image_name = "image_" + str(x) + ".jpg"
        global image
        image = cv2.imread(image_name, 1)
        height, width, channels = image.shape

        if height > width:
            image = imutils.rotate_bound(image, 90)

        #image = imutils.resize(image, height=700)
        Remove_Background(image)
        print(image_name)


if __name__ == "__main__":
    main()
