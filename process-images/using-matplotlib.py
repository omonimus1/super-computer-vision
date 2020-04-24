import numpy as np

import cv2 as cv

from matplotlib import pyplot as plt

img = cv.imread('../media/ragusa.jpeg')
plt.imshow(img, cmap='gray', interpolation='bicubic')
# TO hide tich values on X and Y axis
# plt.xticks([]), plt.yticks([]) 
plt.show()
