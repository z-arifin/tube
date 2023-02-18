import numpy as np
import cv2 as cv

img = cv.imread('WhatsApp Image 2023-01-22 at 20.29.40.jpeg')
img = cv.resize(img, None, fx=0.6,fy=0.6)

"cv.imshow('img', img)"
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv.cornerHarris(gray, 3, 3, 0.230)

dst = cv.dilate(dst, None)

img[dst > 0.01 * dst.max()] = [0, 0, 255]

cv.imshow('dst', img)

cv.waitKey(0)
cv.destroyAllWindows()

'''
Function : cv2.cornerHarris(image,blocksize,ksize,k)
Parameters are as follows :
1. image : the source image in which we wish to find the corners (grayscale)
2. blocksize : size of the neighborhood in which we compare the gradient 
3. ksize : aperture parameter for the Sobel() Operator (used for finding Ix and Iy)
4. k : Harris detector free parameter (used in the calculation of R)
'''