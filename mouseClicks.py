import cv2
import numpy as np

circles = np.zeros((4,2))

counter = 0
def MouseClick(event,x,y,d,s):
    global counter
    if event==cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter = counter+1
        print(x,y)



img = cv2.imread('cardImg.jpg')

while True:
    if counter == 4:
       width, height = 250, 350
       pts1 = np.float32([circles[0], circles[1], circles[2], circles[3]])
       pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])
       matrix = cv2.getPerspectiveTransform(pts1, pts2)
       imgOutput = cv2.warpPerspective(img, matrix, (width, height))
       cv2.imshow("imgOutput", imgOutput)
       counter = 0
    for x in range(0, 4):
        if counter != 0:
            cv2.circle(img, (int(circles[x][0]), int(circles[x][1])), 5, (255, 0, 0), cv2.FILLED)

    cv2.imshow("mouseClick",img)
    cv2.setMouseCallback("mouseClick",MouseClick)
    cv2.waitKey(1)