from PIL import Image

img = Image.open("../media/palermo.jpg")
# Resize the image
resized_img = img.resize((100,100))
resized_img.show()
# Rotate imaage
rotated_img = resized_img.rotate(90)
rotated_img.show()
