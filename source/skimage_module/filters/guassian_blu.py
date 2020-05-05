from skimage import io 
from skimage import filters

img = io.imread('../../media/bwm.jpeg')
filtered_image = filters.gaussian(img, sigma =5)
io.imshow(filtered_image)
io.show()