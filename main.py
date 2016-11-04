# EIASR PALM TRACKING PROJECT

import numpy as np
import cv2

def skin_color(pixel):
    
    Y_min=88
    Y_max=169
    U_min=110
    U_max=114
    V_min=146
    V_max=151
    
    #if pixel[0]>Y_min and pixel[0]<Y_max:
    if pixel[1]>V_min and pixel[1]<V_max:
        if pixel[2]>U_min and pixel[2]<U_max:
            pixel=[241, 128, 128]
            return pixel
    pixel=[49, 128, 128]
    return pixel

img = cv2.imread('hand.png')
width, height, depth = img.shape
output_img = np.zeros((width, height, 3), np.uint8)

output_imgYVU = cv2.cvtColor(output_img, cv2.COLOR_BGR2YCR_CB)
imgYVU = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)

for i in range(0, width):
	for j in range(0, height):
		pixel = imgYVU[i, j]
		output_imgYVU[i, j] = skin_color(pixel)

output_img = cv2.cvtColor(output_imgYVU, cv2.COLOR_YCR_CB2BGR)

cv2.imshow('hand', output_img)
cv2.waitKey(0)