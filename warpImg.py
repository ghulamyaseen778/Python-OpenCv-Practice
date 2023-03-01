import cv2
import numpy as np

width,height = 250,350

img = cv2.imread("cardImg.jpg")
pts1 = np.float32([[492,22],[574,205],[244,144],[324,319]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
# print(pts1[0][0])

# cv2.circle(img,(int(492.0),22),5,(255,0,0),cv2.FILLED)

for x in range(0,4):
    cv2.circle(img,(int(pts1[x][0]),int(pts1[x][1])),5,(255,0,0),cv2.FILLED)

cv2.imshow("card",img)
cv2.imshow("output",imgOutput)
cv2.waitKey(0)
