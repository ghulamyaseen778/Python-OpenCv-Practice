import cv2
print("hello")

img = cv2.VideoCapture(1)
print(img)

while True:
    boool,frame = img.read()
    imgChange = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(frame, 100, 100)
    cv2.imshow("cap",imgCanny)
    if cv2.waitKey(1) == ord('q'):
        break