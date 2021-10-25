import cv2
import numpy as np
import os
from PIL import Image
import image_slicer

im = cv2.imread('pic1.png')

gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# thresh = cv2.threshold(
#     gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
cv2.imshow('gray', im)
cv2.waitKey(0)
