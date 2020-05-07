from matplotlib import pyplot as plot
from skimage import io 
from skimage.color import rgb2gray
from skimage.feature import corner_harris , corner_subpix, corner_peaks

# Read the Image
image = io.imread('../media/bwm.jpeg')
image = rgb2gray(image)

# COmpute the Harris Cornes in the image
# It returns a corner measure response
corners = corner_harris(image)

# Caulcatute the actualt corners in the image
coords = corner_peaks(corners, min_distance=5)

# Decided if the corner point is an edge point or an isolated peak
coord_subpix = corner_subpix(image, coords)

fig, ax = plot.subplots()
ax.imshow(image, interpolation='nearest', cmap=plot.cm.gray)
ax.plot(coords[:, 1], coords[:, 0], '.b', markersize=3)
ax.plot(coord_subpix[:, 1], coord_subpix[:, 0], '+r')
ax.axis((0, 350, 350, 0))
plot.show()