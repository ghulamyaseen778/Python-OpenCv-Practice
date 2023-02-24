import cv2

height,widht=400,400 #height first and second widht

img = cv2.imread("./yaseen.jpg")
print(img.shape,"orignal")

imgResize = cv2.resize(img,(widht,height)) #first widht second height
print(imgResize.shape,"resized")

imgCropped = imgResize[40:250,0:400] #first height second widht
print(imgCropped.shape,"cropped")

cv2.imshow("yaseen",imgCropped)
cv2.waitKey(0)