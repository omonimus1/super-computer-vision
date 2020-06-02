"""
Author: Davide Polliicno
Date: 02/06/2020
Summary: From the default video device, execute a face detection 
    and draw rectangles around your face
"""

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('../cascades/haarcascade_frontalface_alt2.xml')
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame by camera
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ScaleFactor: indicate the accurecy of the face detection
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)
    

    for (x, y, w, h) in faces:
        print(x,y,w,h) # Show the coordinates of my Region of interest (my face)
        roi_gray = gray[y: y+h, x:x+w]

        img_iteam='my-image.png'
        """
        When we stop the program, it will save a picture that will contain
        just our Region of Interest (ROI) - my face
        """
        cv2.imwrite(img_iteam, roi_gray)
    
        # BGR color of the rectangle draw around the face
        color = (255,0,0)
        # Width of the rectangle side
        stroke = 2
        # Create rectangle with specific dimensione using coordinates
        end_coordinate_x = x + w
        end_coordinate_y = y + h
        cv2.rectangle(frame, (x,y,), (end_coordinate_x, end_coordinate_y), color, stroke)

    # Displa the resulting frame
    cv2.imshow('Camera', frame)
    # Wait for 25 ms
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releease capture when the application is over
cap.release()
cv2.destroyAllWindows()