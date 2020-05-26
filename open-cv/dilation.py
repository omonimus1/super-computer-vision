import cv2
import numpy as np

image_to_analize = cv2.imread("../media/animal.jpeg")
kernel = np.ones((40,40), np.uint8)
gray_image = cv2.cvtColor(image_to_analize, cv2.COLOR_BGR2GRAY)
new_image = cv2.dilate(image_to_analize, kernel,  iterations = 1)
cv2.imwrite('dilation_result_color.jpg', new_image)
