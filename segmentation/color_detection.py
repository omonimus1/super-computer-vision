from skimage import measure
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.filters import sobel
import matplotlib.pyplot as plot

# Read an image
img = imread('../media/bwm.jpeg')

# COnvert the imaget o gray scale
img_gray = rgb2gray(img)

# Fond edges in the image
img_edges = sobel(img_gray)

# Find contour in the image
contours = measure.find_contours(img_edges, 0.2)

# Display the image and plot all contours found
fig, ax = plt.subplots()
ax.imshow(img_edges, interpolation='nearest', cmpa= plot.cm.gray)

for n, contour in enumerate(contours):
    ax.plot(contour[:, 1], contour[:, 0], linewidth=2)

ax.axis('image')
ax.set_xticks([])
ax.set_yticks([])

plot.show()