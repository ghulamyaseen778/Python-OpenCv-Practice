import cv2
import numpy as np

height,widht=400,400

img = cv2.imread("./yaseen.jpg")
print(img)

imgResize = cv2.resize(img,(widht,height))
hor = np.hstack((imgResize,imgResize))
ver = np.vstack((imgResize,imgResize))

cv2.imshow("horizontal",hor)
cv2.imshow("vertical",ver)
cv2.waitKey(0)



