from skimage import io 
from skimage import filters
from skimage import color

image_to_analize = io.imread('../media/bwm.jpeg')
# Convert picture from RBG to gray channel
image_to_analize = color.rgb2gray(image_to_analize)
edge_of_the_image = filters.sobel(image_to_analize)
io.imshow(edge_of_the_image)
io.show()