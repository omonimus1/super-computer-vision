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