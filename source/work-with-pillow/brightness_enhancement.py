# Enhance an image modifying its brightenss

from PIL import Image, ImageEnhance
# Get original image to modify
im = Image.open("../media/bwm.jpeg")

enhancer = ImageEnhance.Brightness(im)
# enhancer.enhance(x) -> x: Brightness level
enhanced_im = enhancer.enhance(10)
# Save new updated image
enhanced_im.save("enhanced.bmw.png")
enhanced_im.show()
