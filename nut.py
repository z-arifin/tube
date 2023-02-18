import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    success, image = cap.read()
    if success:
        imgContour = image.copy()
        imgcrop = image#[0:100, 295:560]
        cropCopy = imgcrop.copy()
        imgGray = cv2.cvtColor(imgcrop, cv2.COLOR_BGR2GRAY)
        imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)
        imgCanny = cv2.Canny(imgBlur, 50, 100)
        contours, _ =cv2.findContours(imgCanny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            print(area)
            if area>2000:
                peri=cv2.arcLength(cnt, True)
                print(peri)
                approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
                points=len(approx)
                print(points)
                x,y,w,h=cv2.boundingRect(approx)

    cv2.imshow("Frame", imgCanny)
    #cv2.imshow("Frame", image)
    cv2.imshow("Frame", imgBlur)
    #print(len(corners))

    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()