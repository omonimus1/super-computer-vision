from skimage import io 
from skimage import feature
from skimage import color

image_to_analize = io.imread('../../media/bwm.jpeg')

gray_image = color.rgb2gray(image_to_analize)
edge_detection = feature.canny(gray_image)
io.imshow(edge_detection)
io.show()