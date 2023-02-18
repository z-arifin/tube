import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('WhatsApp Image 2023-01-22 at 20.29.41.jpeg', cv.IMREAD_GRAYSCALE) # `<opencv_root>/samples/data/blox.jpg`
img = cv.resize(img, None, fx=0.6,fy=0.5)

# Initiate FAST object with default values
fast = cv.FastFeatureDetector_create()

# find and draw the keypoints
kp = fast.detect(img,None)
img2 = cv.drawKeypoints(img, kp, None, color=(255,0,0))

# Print all default params
print( "Threshold: {}".format(fast.getThreshold()) )
print( "nonmaxSuppression:{}".format(fast.getNonmaxSuppression()) )
print( "neighborhood: {}".format(fast.getType()) )
print( "Total Keypoints with nonmaxSuppression: {}".format(len(kp)) )
cv.imshow('fast_true.png', img2)

"""# Disable nonmaxSuppression
fast.setNonmaxSuppression(0)
kp = fast.detect(img, None)
print( "Total Keypoints without nonmaxSuppression: {}".format(len(kp)) )
img3 = cv.drawKeypoints(img, kp, None, color=(255,0,0))
cv.imshow('fast_false.png', img3)"""

cv.waitKey(0)
cv.destroyAllWindows()