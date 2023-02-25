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
# rectangleImg=cv2.rectangle(img,(0,0),(100,100),(0,255,0),cv2.FILLED)
# cv2.imshow("LineImg",rectangleImg)


# first point source,
# second point position of circle of both side (x,y)
# third point is radius of circle
# fourth Point is define color
# five point is thickness of line or use cv2.FILLED for fill the triangle
# circleImg=cv2.circle(img,(300,100),50,(0,255,0),3)
# cv2.imshow("circleImg",circleImg)


# first point source,
# second point write own text
# third point is starting point of both side (x,y)
# fourth Point is font family
# five point is font scale
# sixth point is color
# seventh point is thickness
textOnImg=cv2.putText(img,"Ghulam Yaseen",(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),3)
cv2.imshow("textOnImg",textOnImg)


cv2.waitKey(0)
