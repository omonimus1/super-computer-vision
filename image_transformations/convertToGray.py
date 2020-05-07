from PIL import Image

# Load image that we want to convert
img = Image.open("../media/palermo.jpg")
# Convert image in greyscale
gray_image = img.convert("L")
# Show image in greyscale
gray_image.show()
