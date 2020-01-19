import imutils
import numpy as np
import cv2




def red_mask_2_countours(mask):

    img = mask.copy()



    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 5)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        area = cv2.contourArea(box)
        (x, y), (width, height), angle = cv2.minAreaRect(c)
        biggest_size = max(width, height)

        if len(c)>5:
            ellipse = cv2.fitEllipse(c)
            (center, axes, orientation) = ellipse
            majoraxis_length = max(axes)
            minoraxis_length = min(axes)
            eccentricity = (np.sqrt(1 - (minoraxis_length / majoraxis_length) ** 2))
            if area>500:
                if eccentricity < 0.7:
                    cv2.ellipse(original, ellipse, (0, 0, 255), 2)
                else:
                    cv2.drawContours(original, [box], 0, (0, 0, 255), 2)

        else:
            if area>500:
                cv2.drawContours(original, [box], 0, (0, 0, 255), 2)


    #cv2.imshow("red MASK", original)
    #cv2.imshow("img", mask)
    #cv2.waitKey()

def dark_red_mask_2_countours(mask):

    img = mask.copy()



    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 5)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        area = cv2.contourArea(box)
        (x, y), (width, height), angle = cv2.minAreaRect(c)


        biggest_size = max(width, height)

        if len(c)>5:
            ellipse = cv2.fitEllipse(c)
            (center, axes, orientation) = ellipse
            majoraxis_length = max(axes)
            minoraxis_length = min(axes)
            eccentricity = (np.sqrt(1 - (minoraxis_length / majoraxis_length) ** 2))
            if area>320 :
                if eccentricity < 0.7:
                    cv2.ellipse(original, ellipse, (128, 0, 128), 2)
                else:
                    if biggest_size > 50:
                        cv2.drawContours(original, [c], 0, (128, 0, 128), 3)
                        cv2.drawContours(original, [c], 0, (128, 0, 128), -1)
                    else:
                        #cv2.putText(original, str(round(biggest_size, 2)), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)
                        cv2.drawContours(original, [box], 0, (128, 0, 128), 2)

        else:
            if area>320:
                if biggest_size >50 :
                    cv2.drawContours(original, [c], 0, (128, 0, 128), 3)
                    cv2.drawContours(original, [c], 0, (128, 0, 128), -1)
                else:
                    cv2.drawContours(original, [box], 0, (128, 0, 128), 2)
                    #cv2.putText(original, str(round(biggest_size, 2)), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)


    #cv2.imshow("red MASK", original)
    #cv2.imshow("img", mask)
    #cv2.waitKey()

def green_mask_2_countours(mask):

    img = mask.copy()



    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 5)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        area = cv2.contourArea(box)
        (x, y), (width, height), angle = cv2.minAreaRect(c)


        biggest_size = max(width, height)

        if len(c)>5:
            ellipse = cv2.fitEllipse(c)
            (center, axes, orientation) = ellipse
            majoraxis_length = max(axes)
            minoraxis_length = min(axes)
            eccentricity = (np.sqrt(1 - (minoraxis_length / majoraxis_length) ** 2))
            if area>320 :
                if eccentricity < 0.7:
                    cv2.ellipse(original, ellipse, (0, 255, 0), 2)
                else:
                    if biggest_size > 58:
                        cv2.drawContours(original, [c], 0, (0, 255, 0), 3)
                        cv2.drawContours(original, [c], 0, (0, 255, 0), -1)
                    else:
                        #cv2.putText(original, str(round(biggest_size, 2)), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)
                        cv2.drawContours(original, [box], 0, (0, 255, 0), 2)

        else:
            if area>320:
                if biggest_size >58 :
                    cv2.drawContours(original, [c], 0, (0, 255,0), 3)
                    cv2.drawContours(original, [c], 0, (0,255,0), -1)
                else:
                    cv2.drawContours(original, [box], 0, (128, 0, 128), 2)
                    #cv2.putText(original, str(round(biggest_size, 2)), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)


    #cv2.imshow("red MASK", original)
    #cv2.imshow("img", mask)
    #cv2.waitKey()

def orange_mask_2_countours(mask):

    img = mask.copy()



    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 5)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        area = cv2.contourArea(box)
        (x, y), (width, height), angle = cv2.minAreaRect(c)


        biggest_size = max(width, height)

        if len(c)>5:
            ellipse = cv2.fitEllipse(c)
            (center, axes, orientation) = ellipse
            majoraxis_length = max(axes)
            minoraxis_length = min(axes)
            eccentricity = (np.sqrt(1 - (minoraxis_length / majoraxis_length) ** 2))
            if area>550 :
                if eccentricity < 0.7:
                    cv2.ellipse(original, ellipse, (0,140,255), 2)
                else:
                    if biggest_size > 50:
                        cv2.drawContours(original, [c], 0, (0,140,255), 3)
                        cv2.drawContours(original, [c], 0, (0,140,255), -1)
                    else:
                        #cv2.putText(original, str(round(biggest_size, 2)), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)
                        cv2.drawContours(original, [box], 0, (0,140,255), 2)

        else:
            if area>550:
                if biggest_size >50 :
                    cv2.drawContours(original, [c], 0, (0,140,255), 3)
                    cv2.drawContours(original, [c], 0, (0,140,255), -1)
                else:
                    cv2.drawContours(original, [box], 0, (0,140,255), 2)
                    #cv2.putText(original, str(round(biggest_size, 2)), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)


    #cv2.imshow("red MASK", original)
    #cv2.imshow("img", mask)
    #cv2.waitKey()

def yellow_mask_2_countours(mask):

    img = mask.copy()



    thresh = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 5)

    cnts = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        rect = cv2.minAreaRect(c)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        area = cv2.contourArea(box)
        (x, y), (width, height), angle = cv2.minAreaRect(c)


        biggest_size = max(width, height)

        if len(c)>5:
            ellipse = cv2.fitEllipse(c)
            (center, axes, orientation) = ellipse
            majoraxis_length = max(axes)
            minoraxis_length = min(axes)
            eccentricity = (np.sqrt(1 - (minoraxis_length / majoraxis_length) ** 2))
            if area>320 :
                if eccentricity < 0.7:
                    cv2.ellipse(original, ellipse, (0, 255, 255), 2)
                else:
                    if biggest_size < 50:
                        #cv2.putText(original, str(round(biggest_size, 2)), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)
                        cv2.drawContours(original, [box], 0, (0,255,255), 2)

        else:
            if area>320:
                if biggest_size <50 :
                    cv2.drawContours(original, [box], 0, (0, 255, 255), 2)
                    #cv2.putText(original, str(round(biggest_size, 2)), (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, 0, 1)


    cv2.imshow("red MASK", original)
    cv2.imshow("img", mask)
    cv2.waitKey()





def Color_Selection(image):
    img = image.copy()
    img = cv2.bilateralFilter(img,60,75,75)
    #img=cv2.GaussianBlur(img, (5, 5), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    kernel = np.ones((5,5), np.uint8)

    # RED MASK                                                                  -
    red_mask = cv2.inRange(hsv, np.array([0, 120, 20]), np.array([5, 255, 255]))
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    #red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)


    red_mask = imutils.resize(red_mask, height=700)
    red_mask_2_countours(red_mask)

    # DARK RED MASK                                                             -
    dark_red_mask = cv2.inRange(hsv, np.array([169, 160, 20]), np.array([179, 255, 255]))
    dar_red_mask = cv2.morphologyEx(dark_red_mask, cv2.MORPH_OPEN, kernel)
    dark_red_mask = cv2.erode(dark_red_mask,kernel,iterations = 1)

    dark_red_mask = imutils.resize(dark_red_mask, height=700)
    dark_red_mask_2_countours(dark_red_mask)

    # GREEN MASK                                                                -
    green_mask = cv2.inRange(hsv, np.array([33, 92, 20]), np.array([63, 255, 255]))
    green_mask = cv2.morphologyEx(green_mask, cv2.MORPH_OPEN, kernel)
    green_mask = cv2.dilate(green_mask,kernel,iterations = 1)

    green_mask = imutils.resize(green_mask ,height=700)
    green_mask_2_countours(green_mask)

    # ORANGE MASK                                                                -
    orange_mask = cv2.inRange(hsv, np.array([10, 120, 20]), np.array([20, 255, 255]))
    orange_mask = cv2.morphologyEx(orange_mask, cv2.MORPH_OPEN, kernel)
    orange_mask = cv2.dilate(orange_mask,kernel,iterations = 1)
    orange_mask = cv2.erode(orange_mask,kernel,iterations = 1)


    orange_mask = imutils.resize(orange_mask, height=700)
    orange_mask_2_countours(orange_mask)



    # YELLOW MASK                                                                  -
    yellow_mask = cv2.inRange(hsv, np.array([20, 110, 20]), np.array([30, 255, 255]))
    yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel)
    #red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_CLOSE, kernel)


    yellow_mask = imutils.resize(yellow_mask, height=700)
    yellow_mask_2_countours(yellow_mask)



    img = imutils.resize(img, height=700)
    #cv2.imshow("img", original)
    #cv2.imshow("mask", green_mask)
    #cv2.waitKey()


def main():
    print("hello world")
    for x in range(46):
        image_name = "image_" + str(x) + ".jpg"
        global image
        global original


        image = cv2.imread(image_name, 1)

        height, width, channels = image.shape


        if height > width:
            image = imutils.rotate_bound(image, 90)

        image = imutils.resize(image, height=1000)

        original = imutils.resize(image.copy(), height=700)
        print(image_name)
        Color_Selection(image)



if __name__ == "__main__":
    main()
