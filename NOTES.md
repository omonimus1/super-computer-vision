## Computer Vision

Computer vision can be applied in social platforms, medicine, autonomous driving, security and many other fields

### Python Modules

Pillow (PIl): Python imaging Library. 
``` pip install pillow```

Cropping: means extract a particular region of the image, which is smaller than original image. The region extracted by the crop operation is called ROI: Region Of Interest. A ROI can be extremelly useful when we want to apply our algorithm in a specific section of the image. 


```
from PIL import Image

# Load original picture
img = Image.open("media/palermo.jpg")
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
```

## Changing color 

There are different color spaces:
* Grayscale: Each pixel has a value between 0 and 255. 0 is black and 255 is white. 
* Red green Blue (RGB): each pixel is a combinatyion of three values, each rapresenting a color in rd, green and black (255, 255, 255) for example.
* Hue, Saturation, Value (HSV): Cylindrical coordinate system where we project RGB values onto a cylinder. The HSV scale allows us to change the shades by carying values and saturations. 

Image depth or color depth: number of bits used to represent a color of a pixel. 
```
from PIL import Image

# Load image that we want to convert
img = Image.open("media/palermo.jpg")
# Convert image in greyscale
gray_image = img.convert("L")
# Show image in greyscale
gray_image.show()
```

### Geometrical transformation

```
from PIL import Image

img = Image.open("media/palermo.jpg")
# Resize the image
resized_img = img.resize((100,100))
resized_img.show()
# Rotate imaage
rotated_img = resized_img.rotate(90)
rotated_img.show()
```

### Image enhancement

```
# Change the Brightness of an image
from PIL import Image, ImageEnhance
# Get original image to modify
im = Image.open("media/bwm.jpeg")

enhancer = ImageEnhance.Brightness(im)
# enhancer.enhance(x) -> x: Brightness level
enhanced_im = enhancer.enhance(10)
# Save new updated image
enhanced_im.save("enhanced.bmw.png")
enhanced_im.show()
```

With ImageEnhance we can also modify the contrast of the image. 

### Access / Modify pixels

```
import PixelAccess
```
PixelAccess is a python class mostly used for its two main methods:
* getpixel(): return the color value of the pixel at the (x,y) coordinates. ```print(img.getpixel(100,100))```
* putpixel(): changes the ciolor value of the pixel at the x, y, using the RGB colors. ``` img.putpixel((100,100),(20.230.145))`` -> This means, assign the color created by the conbination of 20red, 230 Green and 145 blue in the pixel present at the position of cordinates X=100 and Y=100

## Scikit-image

This library works with image with float pixels (where every pixel has a value between 0 and 1).
```pip install scikit-image```

In Scikit-image, an image can be read using the imread() function, that returns a N Dimensional array. 



