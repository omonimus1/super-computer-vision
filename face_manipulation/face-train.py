import os
# Python Library Image
from PIL import Image
import numpy as np
import cv2
import pickle

face_cascade = cv2.CascadeClassifier('../cascades/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

# Get the path of this face-train.py path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)
image_dir = os.path.join(BASE_DIR, "images")

current_id = 0
label_ids = {}
y_labels = []
x_train =  []

for root, dirs, files in os.walk(image_dir):
    for file in files:
        if file.endswith("png") or file.endswith("jpg") or file.endswith("jpeg"):
            path = os.path.join(root, file)
            # Fetch directory name of our image and replace any whitespace with "-"
            label = os.path.basename(os.path.dirname(path)).replace(" ", "-").lower()
            # print('path', path, '---label', label)
            if label in label_ids:
                pass
            else:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            
            # print(label_ids)
            # y_labels.append(label)
            # x_train.append(path)

            # TRAINING SECTION

            # Convert to grayscale
            pil_image = Image.open(path).convert("L") 
            # Resize image
            size = (550,500)
            # Keep same quality of the image
            final_image = pil_image.resize(size, Image.ANTIALIAS)
            # Convert any image pixel in a number (unsigned int)
            image_array = np.array(final_image, "uint8")
            # Print array of pixels values
            # print(image_array)
            faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.5, minNeighbors=5)
            for(x,y,w,h) in faces:
                roi = image_array[y: y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)


# print(x_train)
# print(y_labels)

with open('labels.picle', 'wb') as f:
    pickle.dump(label_ids, f)


recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")