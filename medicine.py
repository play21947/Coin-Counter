import cv2
import numpy as np

img = cv2.imread("./image.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray_blur = cv2.GaussianBlur(gray_img, (15, 15), 0)
threshold = cv2.adaptiveThreshold(gray_blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 1)
kernel = np.ones((3,3),np.uint8) #unit8 is data type
closing = cv2.morphologyEx(threshold, cv2.MORPH_CLOSE, kernel, iterations=5)



#1 Find border 2 make it soft
contours, hierachy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

counter = 0

for i in contours:
    area = cv2.contourArea(i)
    print(area)
    if area > 30000 and area < 70000:
        test = cv2.fitEllipse(i)
        print('test : ', test)
        counter = counter + 1
        cv2.ellipse(img, test, (0, 255, 0), 2)
    
cv2.putText(img, str(counter), (200, 100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 5, (0, 0, 255), 2)

cv2.imshow("titile", img)
cv2.waitKey(0)
cv2.destroyAllWindows()