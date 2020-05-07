from PIL import Image
from PIL import ImageFilter


# Fetch original image
img = Image.open('../media/bwm.jpeg')
# Show original image
img.show()
# Apply the Guassian Blur filter to the image
filterd_image = img.filter(ImageFilter.GaussianBlur)
# Show filtered image
filterd_image.show()
