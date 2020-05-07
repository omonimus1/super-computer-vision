from skimage import io
from skimage import morphology

original_image = io.imread('../media/palermo.jpg')
eroded_image = morphology.binary_erosion(original_image)
io.imshow(eroded_image)
io.show()
