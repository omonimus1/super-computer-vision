from PIL import Image
from PIL import ImageFilter

original_image = Image.open('../media/bwm.jpeg')
filtered_image = original_image.filter(ImageFilter.MedianFilter(7))
filtered_image.show()
