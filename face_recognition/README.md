## Face recognition

### Foundamental Concepts

* **Pickel:** modules used for serialization and deserialize a Python object structure. It convert a Python object into a byte stream to store it in a file/database. Pickling is a way to convert a python object (list, dict, etc.) into a character stream. 
* **Color convertion:** every operation like edge detection, object detection, corned detection requires an image in graysclale. 
* **How is safe use Face Recognition**: personally, using very recents pictures, it' easy to break a face recognition app with an image of the person that we want to recognize. 

### How train you model

1. Add pictures of the people that you want to recognize in the ```media/``` folder, in personal folders. 
![Images structure](../tutorial_medias/train-model.png)
2. Run face-train.py file to train your own model ```python face-train.py```
3. Run face-recognition.py to get video input and do live face recognition  ``` python face-recognition.py ```

