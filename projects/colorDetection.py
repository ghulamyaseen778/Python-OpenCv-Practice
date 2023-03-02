import cv2
import numpy as np

def emapty(a):
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",640,240)
cv2.createTrackbar("Hue Min","HSV",0,179,emapty)
cv2.createTrackbar("Sat Min","HSV",0,255,emapty)
cv2.createTrackbar("Value Min","HSV",0,255,emapty)
cv2.createTrackbar("Hue Max","HSV",179,179,emapty)
cv2.createTrackbar("Sat Max","HSV",255,255,emapty)
cv2.createTrackbar("Value Max","HSV",255,255,emapty)


framewdith = 640
frameheight = 480

cap = cv2.VideoCapture(1)
cap.set(3,framewdith)
cap.set(4,frameheight)

while True:
    _,img = cap.read()
    imgHsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min","HSV")
    s_min = cv2.getTrackbarPos("Sat Min","HSV")
    v_min = cv2.getTrackbarPos("Value Min","HSV")
    h_max= cv2.getTrackbarPos("Hue Max","HSV")
    s_max = cv2.getTrackbarPos("Sat Max","HSV")
    v_max = cv2.getTrackbarPos("Value Max","HSV")

    cv2.imshow("colorImg",img)
    cv2.imshow("hsvImg",imgHsv)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
