'''
opencv2
numpy

'''
import numpy
from opencv import cv, cv2

import cv2
import numpy as np
from matplotlib import pyplot as plt

template = cv2.imread("Bernie.png")
image = cv2.imread("puzzlePic.png")

res = cv2.matchTemplate(image,template,cv2.TM_CCOEFF)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

bottom_left = [0,0]
top_right = [0,0]

print("Max Value: " , str(max_loc))

w, h,c = template.shape[::-1]


final = cv2.rectangle(image,max_loc, (max_loc[0] + 16, max_loc[1] + 22),255,10)

cv2.imwrite("final.png",final)