"""
Author: Davide Pollicino 
Date: 01/06/2020
Summary: Open camera stream and show it
"""
import cv2

# capture frames from a camera
cap  = cv2.VideoCapture(0)

# loop runs if capturing has been initialized
while(1):
    # Read frame from a camera
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow('Camera', frame)

    # Wait for 25 ms
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera from video capture
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()