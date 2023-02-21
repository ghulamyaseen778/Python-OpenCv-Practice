import cv2
print("hello")

img = cv2.VideoCapture(1)
print(img)

while True:
    boool,frame = img.read()
    cv2.imshow("cap",frame)
    if cv2.waitKey(1) == ord('q'):
        break