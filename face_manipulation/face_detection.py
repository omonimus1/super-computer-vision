import cv2

# Load cascade face dection .xml file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# capture frames from a camera
cap  = cv2.VideoCapture(0)

# loop runs if capturing has been initialized
while(1):
    # Read frame from a camera
    ret, frame = cap.read()
    # Convert to gray for object detection
    gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+w), (255,0,0),2)

      # Display the frame
    cv2.imshow('Camera', frame)
    
    # Wait for 25 ms
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera from video capture
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()