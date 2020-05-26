import cv2

image_to_analize = cv2.imread("../../media/animal.jpeg")
# Conver to gray
gray = cv2.cvtColor(image_to_analize, cv2. COLOR_BG2GRAY)
# Apply the Sobel algorithm for thje efge detectin
x_edges = cv2.Sobel(gray, 1,1,0, ksize=5)
# Store image result
cv
