import numpy as np
import cv2

image = cv2.imread('WhatsApp Image 2023-01-22 at 20.29.41.jpeg')

image = cv2.resize(image, None, fx=0.6,fy=0.5)
#image = image[0:500, 100:250]
#cv2.imshow('img', image)
#Converting to grayscale
gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#Specifying maximum number of corners as 1000
# 0.01 is the minimum quality level below which the corners are rejected
# 10 is the minimum euclidean distance between two corners
corners_img = cv2.goodFeaturesToTrack(gray_img,1000,0.07,10)
"""if len(corners_img) > 10:
    corners_img = cv2.goodFeaturesToTrack(gray_img,1000,0.9,10)"""

corners_img = np.int0(corners_img)

for corners in corners_img:
    
    x,y = corners.ravel()
    #Circling the corners in green
    cv2.circle(image,(x,y),3,[0,255,0],-1)

cv2.imshow('dst', image)

print(len(corners_img))

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
Function: cv2.goodFeaturesToTrack(image,maxCorners, qualityLevel, minDistance[, corners[, mask[, blockSize[, useHarrisDetector[, k]]]]])
image – Input 8-bit or floating-point 32-bit, single-channel image.
maxCorners – You can specify the maximum no. of corners to be detected. (Strongest ones are returned if detected more than max.)
qualityLevel – Minimum accepted quality of image corners.
minDistance – Minimum possible Euclidean distance between the returned corners.
corners – Output vector of detected corners.
mask – Optional region of interest. 
blockSize – Size of an average block for computing a derivative covariation matrix over each pixel neighborhood. 
useHarrisDetector – Set this to True if you want to use Harris Detector with this function.
k – Free parameter of the Harris detector.
'''