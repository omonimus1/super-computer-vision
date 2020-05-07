from PIL import Image

# Load original picture
img = Image.open("../media/palermo.jpg")
img.show()

# Print format and size of the original picture
print(img.format)
print(img.size)

# Set dimension of the ROI
dim = (0, 0,50,50)
# Extract ROI
crop_img = img.crop(dim)
crop_img.save("media/crop.jpg")
crop_img.show()
