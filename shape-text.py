import cv2
import numpy as np

img= np.zeros((512,512,3),np.uint8)

# img[0:212,0:512]=255,255,0 #for sepecific Img , first Height and second widht
# img[:]=255,255,0 #for whole Img
# cv2.imshow("blankImg",img)

# first point source,
# second point starting point of both side (x,y)
# third point ending point of both side (x,y)
# fourth Point is define color
# five point is thickness of line
# LineImg=cv2.line(img,(0,0),(200,100),(0,255,0),2)
# cv2.imshow("LineImg",LineImg)

# first point source,
# second point starting point of both side (x,y)
# third point is area of triangle (x,y)
# fourth Point is define color
# five point is thickness of line or use cv2.FILLED for fill the triangle
rectangleImg=cv2.rectangle(img,(0,0),(100,100),(0,255,0),cv2.FILLED)
cv2.imshow("LineImg",rectangleImg)
cv2.waitKey(0)
