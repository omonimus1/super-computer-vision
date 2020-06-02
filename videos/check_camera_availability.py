import cv2

def testDevice(source):
    cap = cv2.VideoCapture(source)
    if cap is None or not cap.isOpened():
        print('Warning: unable to open vide source: ', source)


# Test Default camera device
testDevice(0)
# Test webcame of the laptop
testDevice(1)