import cv2
import numpy as np 

image_to_analize = cv2.imread("../media/bwm.jpeg")
ker = np.ones((5,5), np.uint8)
# Apply erosion to the image
new_image = cv2.erode(image_to_analize, ker, iterations = 1)
# Store the new image 
cv2.imwrite("erosion.jpg", new_image)