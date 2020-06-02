# Face Detection

* Detection works only on grayscale images. 
```
# Convert to gray for object detection
gray = cv2.cvtColor(frame,  cv2.COLOR_BGR2GRAY)
```

* detectMultiScale: used to detect the faces. 
Arguments(): 
- input image
- scaleFactor: idnicates how miuch the image size is reduces with each scale
- minNeighbours: how many neighbors each candeicate rectangle should have to retain it. 

# Face detection 

For my trainign I have use face-recognition module.
The base idea is to localize the most important landmarks of a face: eyes, nose, mouth and chin. 
face-recognition can be used for face detection or also to add mackup to the image provided. 


### Speed up face detection operations

We can dedicated a specific numbers of cores to speed up our face detection elaboration. 
```
--cpus <number_of_cpu_cores_to_use>
```
