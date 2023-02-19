import cv2
import numpy as np

cap = cv2.VideoCapture('test3.mp4')

while True:
    success, image = cap.read()
    #imgContour = image.copy()
    imgCrop = image.copy()#image[0:100, 295:568]
    cropCopy = imgCrop.copy()
    imgGray = cv2.cvtColor(imgCrop, cv2.COLOR_BGR2GRAY)
    corners_img = cv2.goodFeaturesToTrack(imgGray,1000,0.07,10)
    if len(corners_img) > 10:
        corners_img = cv2.goodFeaturesToTrack(gray_img,1000,0.9,10)

    corners_img = np.int0(corners_img)

    for corners in corners_img:

        x,y = corners.ravel()
        #Circling the corners in green
        cv2.circle(image,(x,y),3,[0,255,0],-1)
        print(len(corners_img))
    
    cv2.imshow('dst', image)

    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()