"""Project for EIASR class. WUT, year 2016/2017"""

import numpy as np
import argparse
import cv2

"""
Runs the backprojection algorithm. 
The output is a image showing the detected object in black and white and also with applied color histagram.

target - target image
"""
def backprojection(target):

    hsvt = cv2.cvtColor(target,cv2.COLOR_BGR2HSV)

    height, width, depth = target.shape

    # finding the region of interest
    roi = target[height / 2 - 40 : height / 2 + 40, width / 2 - 40 : width / 2 + 40]
    hsv = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

    # debug
    #cv2.imshow('hand', roi)
    #cv2.waitKey(0)

    # calculating object histogram
    roihist = cv2.calcHist([hsv],[0, 1], None, [180, 256], [0, 180, 0, 256] )

    # normalize histogram and apply backprojection
    cv2.normalize(roihist,roihist,0,255,cv2.NORM_MINMAX)
    dst = cv2.calcBackProject([hsvt],[0,1],roihist,[0,180,0,256],1)

    # Now convolute with circular disc
    disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
    cv2.filter2D(dst,-1,disc,dst)

    # threshold and binary AND
    ret,thresh = cv2.threshold(dst,50,255,0)
    thresh = cv2.merge((thresh,thresh,thresh))
    res = cv2.bitwise_and(target,thresh)

    res = np.vstack((target,thresh,res))
    cv2.imwrite('res.jpg',res)


def main():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", help = "path to the image")
    args = vars(ap.parse_args())

    # load the image
    image = cv2.imread(args["image"])

    backprojection(image)


if __name__ == "__main__":
    main()