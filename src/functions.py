import cv2
import numpy as np
import time


def funcErode(file):
	img = cv2.imread(file)
	start = time.time()
	kernel = np.ones((5, 5), np.uint8)
	erode = cv2.erode(img, kernel)
	cv2.imshow("erodeRes", erode)
	cv2.waitKey()
	stop = time.time()
	action_time = stop - start
	print(f"{action_time} s\n")


def funcBinary(file):
	img = cv2.imread(file)
	start = time.time()
	grey_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	_, threshold_image = cv2.threshold(grey_image, 125, 255, cv2.THRESH_BINARY)
	cv2.imshow("binaryRes", threshold_image)
	cv2.waitKey()
	stop = time.time()
	action_time = stop - start
	print(f"{action_time} s\n")


def funcDilate(file):
	img = cv2.imread(file)
	start = time.time()
	kernel = np.ones((5, 5), np.uint8)
	dilate = cv2.dilate(img, kernel)
	cv2.imshow("dilateRes", dilate)
	stop = time.time()
	action_time = stop - start
	print(f"{action_time} a\n")


def funcBoxFilter(file):
	img = cv2.imread(file)
	start = time.time()
	boxFilter = cv2.boxFilter(img, -1, (5, 5))
	cv2.imshow("boxFilterRes", boxFilter)
	cv2.waitKey()
	stop = time.time()
	action_time = stop - start
	print(f"{action_time} s\n")


def funcMedian(file):
	img = cv2.imread(file)
	start = time.time()
	median = cv2.medianBlur(img, 5)
	cv2.imshow("medianRes", median)
	cv2.waitKey()
	stop = time.time()
	action_time = stop - start
	print(f"{action_time} s\n")