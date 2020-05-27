# OpenCV Notes

OpenCV:
* computer vision open-source and cross-platform library.
* It allows to run C.V. algorithms in run time. 
* Interoperable with scientific libraries such as NumPY and SciPy.

imread(): returns an image in BGR coloe format, even if the file uses a grayscale format.
BGR(blue-green-red): represents the same color space as RGB(red-green-blue):but  the byte order is reserved.

```
import cv2

grayImage = cv2.imread('MyPic.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('MyNewPicGray.png', grayImage)
```

OpeCV image: is a 2D or 3D array. 
Byte: can contains a vale between 0 to 255.

## Face detection

```
import cv2

# Load the cascadeclassifier
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Read Image input
img = cv2.imread('face.jpg')
# cv2.imshow('myface', img)
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces

faces = face_cascade.detectMultiScale(gray, 1.1 , 4)
# Draw rectangle arond each face

# 10 is the width of the rectangles drwan on the face
# (255,0,0) is the colo in rgb of th r
for(x,y , w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, x+h), (255,0,0), 10)   

# Display Output
cv2.imshow('img', img)
cv2.waitKey()
```

If we need, we can also introduce mutliple Cascade classifier filters at the same time like:
* Front face
* Eye detection 
* Moth detection  and others

### How face Open CV's face recognition works

1. Get input image
2. Detect edges and face recognitions using facial landmarks like eyes, eyebrows, nose, mouth, jawline etc... 
3. Crop the image: removal of unwanted outer areas from a photographic or illustrated image









