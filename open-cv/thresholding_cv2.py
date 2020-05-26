"""
Author: Davide POllicino
Date: 11/05/2020
"""
import cv2
image_to_analize = cv2.imread("../media/animal.jpeg")
gray_image = cv2.cvtColor(image_to_analize, cv2.COLOR_BGR2GRAY)
new_img = cv2.threshold(gray_image,120,255,cv2.THRESH_BINARY)
cv2.imwrite("thresholding.jpg", new_img[1])
cv2.waitKey(10)