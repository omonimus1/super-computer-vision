import numpy as np

import cv2 as cv

# Load an image , the 0 paramenteer will convert the img in black and white
img = cv.imread_unchanged('../media/palermo.jpg')

# Show the image in a window
cv.imshow('image', img)

# Store the image locally
cv.imwrite('stored-pic.jpg', img)

cv2.waitKey(10)
cv2.destroyAllWindows()
