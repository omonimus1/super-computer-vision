from scipy import ndimage as ndi
from skimage.morphology import watershed, disk
from skimage import data
from skimage.io import imread
from skimage.filters import rank
from skimage.color import rgb2gray
from skimage.util import img_as_ubyte

image_to_analize = data.astronaut()
gray_image = rgb2gray(image_to_analize)

image = img_as_ubyte(gray_image)
# Calulcate the local gradiantes of the image
# and select only points with gradiants value of < 20
markers = rank.gradient(image, disk(5)) < 20
markers = ndi.label(markers)[0]

gradient = rank.gradient(image, disk(2))

# Waterhe algorithm
labels = watershed(gradient, markers)