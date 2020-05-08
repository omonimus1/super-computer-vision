"""
Superpixel is a color detection tecnique that does not analize every possible 
pixel of the image but remove redundancy in the pixels of an image, trying to 
combining pixels closer to each other that have the same color value into a cluster 
and then call those clusters superpixels.  
"""
from skimage import segmentation, color
from skimage import io
from skimage.future import graph
from matplotlib import pyplot as plt
img = io.imread('../media/animal.jpeg')

img_segments = segmentation.slic(img, compactness=10, n_segments=700)
superpixel_image = color.label2rgb(img_segments, img, kind='avg')

io.imshow(superpixel_image)
io.show()