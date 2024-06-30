###from PIL import Image

from PIL import Image, ImageFilter
 
 
# Opening the image (R prefixed to string
# in order to deal with '\' in paths)
image = "testPhoto.png"
 
# Converting the image to grayscale, as edge detection 
# requires input image to be of mode = Grayscale (L)
#image = image.convert("L")
 
# Detecting Edges on the Image using the argument ImageFilter.FIND_EDGES
#image = image.filter(ImageFilter.FIND_EDGES)
 
# Saving the Image Under the name Edge_Sample.png
def applyEffect(pic, function):
    img = Image.open(pic)
    imageNew = Image.new("RGB", (img.size[0], img.size[1]))
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixel = img.getpixel((x, y))
            
            
            imageNew.putpixel((x,y), function(pixel))
    imageNew.save("newpic.jpg")
    return imageNew.show()

def findYellow(pixel):
    r, g, b = pixel[0], pixel[1], pixel[2]
    if r > 145 and r < 209 and g > 129 and g < 190 and b > 50 and b < 138:
        return (0,0,0)
    else:
        return (255,255,255)

def nut(pixel):
    return 0

def ballCheck(pixel):
    return 0

class Balls():
    
    def __init__(self, size, color, location):
        super(Balls, self).__init__(size, color, location)
        self.size = 0
        self.color = (0,0,0)
        self.location = []
    
applyEffect(image, findYellow)
image.save(r"photoTestEnd.png")