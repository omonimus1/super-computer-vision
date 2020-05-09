import cv2

img = cv2.imread("../media/animal.jpeg")
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("My gray image", gray_image)
cv2.imwrite("../media/gray_image.jpeg", gray_image)

