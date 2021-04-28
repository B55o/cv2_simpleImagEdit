import cv2
import numpy as np


def funcErode(file):
	img = cv2.imread(file)
	kernel = np.ones((5, 5), np.uint8)
	erode = cv2.erode(img, kernel)
	cv2.imwrite(f"res_{file}_erode.jpg", erode)


def funcBinary(file):
	img = cv2.imread(file)
	grey_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	_, threshold_image = cv2.threshold(grey_image, 125, 255, cv2.THRESH_BINARY)
	cv2.imwrite(f"res_{file}_binary.jpg", threshold_image)


def funcDilate(file):
	img = cv2.imread(file)
	kernel = np.ones((5, 5), np.uint8)
	dilate = cv2.dilate(img, kernel)
	cv2.imwrite(f"res_{file}_dilate.jpg", dilate)


def funcBoxFilter(file):
	img = cv2.imread(file)
	boxFilter = cv2.boxFilter(img, -1, (5, 5))
	cv2.imwrite(f"res_{file}_Box_filter.jpg", boxFilter)


def funcMedian(file):
	img = cv2.imread(file)
	median = cv2.medianBlur(img, 5)
	cv2.imwrite(f"res_{file}_median.jpg", median)


# funcErode()
# funcBinary()
# funcDilate()
# funcBoxFilter()
# funcMedian()
