import cv2

videoCapture = cv2.VideoCapture('MyInputVid.avi')
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)

size = (int (videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter(
    'OutputVideo.avi', cv2.cv.CV_FOURCC('I', '4', '2', '0'), fps, size)

sucess, frame = videoCapture.read()
while success:
    # Loop until there are not frames
    videoWriter.write(frame)
    sucess, frame = videoCapture.read()

    