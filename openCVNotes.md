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


### Convert between image and raw bytes

Image in OpenCV is a 2D or 3D array of type numpy.array.
8-bit grayscale: 2d array representing an image, where each element of the 2D array contains a byte value. 

**imread** return a BGR color format. It represent the same color of RGBV but the byte order is reserved. 
**imwrite**:  requires an image to in BGR or grayscale format. 
```
import cv2

grayImage = cv2.imread('pic.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)
cv2.imwrite('MyGrayPicture.png', grayImage)
```
**urandom()**: generates random bytes in python (part of the os module). 


### Caputure frames from multiple camera in OpenCV

read() is not good when managing and synchronize a set of cameras or a multi-head camera (sch as Kinect or stereo camera). 


**PIL image memory**: ImageGrab.grab() -> takes a snapshot of the screen. 

**Multiple-camera setup:** set of cameras used for the same scene (probably from different angles, as in a film set).


We use grab() and retrieve instead().
```
sucess = cameraCapture0.grab()
if success:
    frame0 = cameraCapture0.retrieve()

# In case of multi-head camera, we need to indicate th index
sucess1 = multiHeadCameraCapture.grab()
if sucess1:
    frame1 = multiHeadCameraCapture.retrieve(channel = 1)
```

### enterFrame() and exitFrame()

* enterFrame():
* exitFrame():

OpenCV does not officially support any method for check the frame-rate of a camera, but if we want, we can help ourself using time.time to solve this issue and know better the performances of our camera. 


### Haar Cascades

The Haar Cascade classifiers, which analyze contrast between adjacent image regions to determine whether or not a ROI is a matched type(eyes, nose and mouth).

Images contains lots of details that tends to be unstable with respect to varations in lighting, viewing angle, distance, camera shake and digital noise.

For any frame, features (details of the face), may depending on the regions' size, which may be called the **windows size**.
Two images that differen only in scale should have same features  even for multiple window sizes. Such a collection of features in called a **cascade**.

Upside-down face is not considered similar to an uprights face and a face viewd in profile is not considered similar to a face viewed from the front. 

All cascades require a frontal, upright view od the subject. 

### Rectagle, CascadeClassifier, scaleFactor and minNeighbours

* **scaleFactor:** high value improves performance but diminishes robustness with respect to variations in scale. 
* **minNeighbours**: is one less that the minimum number of regions that are required in a match; 
* **detectMultiScale:** is a list of match, each expresses as a rectangle in format[x,y, w, h];
```
# Capture frame-by-frame
ret, frame = cap.read()
gray  = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=7)
```

OpenCV provides the rectangle() function for drawing;
```
color = (255, 0, 0) #BGR 0-255 -> It will be a blue rectangle
    stroke = 2
    end_cord_x = x + w
    end_cord_y = y + h
    cv2.rectangle(frame, (x, y), (end_cord_x, end_cord_y), color, stroke)
```
A CascadeClassifier is initialized witha cascade data. 
```
eye_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_eye.xml')
smile_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_smile.xml')
```
## Check if a frame is gray

Color images are 3D arrays, while grayscale images have fewer dimensions;
```
def isImageGray(image):
    # Return True if the image has one channel per pixel
    return image.ndmi < 3
```


