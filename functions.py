import cv2
import numpy as np

# make kernal [0]
kernal =np.ones((5,5),np.uint8)
print(kernal)

img=cv2.imread("./yaseen.jpg")

# make gray img [1]
img1=cv2.imread("./yaseen.jpg",0)
# cv2.imshow("yaseen",img1)

# change img color using cvt [2]
# imgChange = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow("imgChange",imgChange)

# make blur img [3]
# imgBlur = cv2.GaussianBlur(img,(5,5),0)
# cv2.imshow("imgBlur",imgBlur)

# make canny img [4]
# imgCanny = cv2.Canny(img,100,100)
# cv2.imshow("imgBlur",imgCanny)

# make canny and dillation img,make thick canny lines [5]
# imgCanny = cv2.Canny(img,100,100)
# imgDillation = cv2.dilate(imgCanny,kernal,iterations=2)
# cv2.imshow("imgDillation",imgDillation)

# make canny,dillation,Eroded img,make silme dillation lines [6]
imgCanny = cv2.Canny(img,100,100)
imgDillation = cv2.dilate(imgCanny,kernal,iterations=2)
imgEroded = cv2.erode(imgDillation,kernal,iterations=2)
cv2.imshow("imgEroded",imgEroded)


cv2.waitKey(0)
