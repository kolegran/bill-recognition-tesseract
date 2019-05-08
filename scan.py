import numpy as np
import cv2
from skimage.filter import threshold_adaptive
from transform import four_point_transform

import argparse
import imutils

def preprocess_image():
	image = cv2.imread("bills/molinary.jpg")
	ratio = image.shape[0] / 500.0
	orig = image.copy()
	image = imutils.resize(image, height = 500)
 
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (5, 5), 0)
	edged = cv2.Canny(gray, 75, 200)

	cv2.imwrite("bills/result/bill-test.jpg", edged)

preprocess_image()
