import cv2
import numpy as np

img= np.zeros((512,512,3),np.uint8)

# img[0:212,0:512]=255,255,0 #for sepecific Img , first Height and second widht
img[:]=255,255,0 #for whole Img
cv2.imshow("blankImg",img)
cv2.waitKey(0)