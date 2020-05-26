"""
Author: Davide Pollicino 
Date: 11/05/2020
Summary: Fetch a ROI(Region of intereste of an image) i using the crop function
"""

import cv2

# Fetch image
image_to_analize = cv2.imread('../media/animal.jpeg')
roi = image_to_analize[0:100, 40:350]
cv2.imwrite('../media/image_cropped_cv2.jpeg', roi)
cv2.imshow("CroppedPic", roi)
cv2.imshow("Original Image", image_to_analize)
cv2.waitKey(0)