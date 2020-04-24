## Requirements

* Numpy ```pip3 install numpy```
* [CV2: Linux demo installation](https://docs.opencv.org/3.4/d2/de6/tutorial_py_setup_in_ubuntu.html) 
* matplotlib

#### Numpy

General-purpse array-processing package, with high performance with multiple arrays (remember, an image is a 2D: array).

Numpy can be used to integrate also C/c++ and Fortran code.

#### Matplotilib

Python library that allows to manipulate an image, modifying it's properties, style, zoom in and zoom out. 

#### CV2
OpenCV-Python is a library designed to solve computer vision problems.

### CV:  Show an image

 ````
import numpy as np

import cv2 as cv

# Load an image , the 0 paramenteer will convert the img in black and white
img = cv.imread('../media/palermo.jpg')

# Show the image in a window where: 
# 1rst parameter is the window title and the 2nd is the image to show

cv.imshow('image', img)
 ```

Fetch an image:
```
# Fetch the image and show it gray scale
cv2.imread('mypic.png', 0)
# OR
cv2.imread_grayscale('mypic.pnj')  
```
```
# Fetch the image and show it with it's origina colors
cv2.imread('mypic.png', 1)
# OR
cv2.imread_color('mypic.png')

```