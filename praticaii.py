from urllib.request import urlopen
from PIL import Image # package pillow
import math

# Task 1 -> Reduce the resolution of the image to half the height 
# and width of the  rgb.png  image and display this image.
def reduceResolution(img):
    img_new = Image.new( "RGB", (math.floor(img.size[0]/2), math.floor(img.size[1]/2)))
    raster_new = img_new.load()
    for i in range(math.floor(img.size[0]/2)):
        for j in range(math.floor(img.size[1]/2)):
            raster_new[i,j] = img.getpixel((2 * i, 2 * j))
            
    return(img_new)


# Task 2 -> Convert rgb.png image to grayscale and display it.
def grayScale(img):
    img_new = Image.new( "L", (img.size[0], img.size[1]))
    raster_new = img_new.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            (r, g, b, _) = img.getpixel((i, j))
            raster_new[i,j] = int(0.3 * r + 0.59 * g +  0.11 * b)
            
    return(img_new)

# Task 3-> Transform rgb.png image   into binary image and display it.
def blackAndWhite(img):
    img_new = Image.new( "1", (img.size[0], img.size[1]))
    raster_new = img_new.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            (r, g, b, _) = img.getpixel((i, j))
            key = int(0.3 * r + 0.59 * g +  0.11 * b)
            if key <= 127:
                raster_new[i,j] = 0
            else:
                raster_new[i,j] = 1
           
    return(img_new)

# Task 4-> Reduce the number of bits per pixel of the  rgb.png image to 3 bits. 
# Tip: To do this, perform a binary operation to keep only the 3 most significant 
# bits of each color component. For example, an R channel of 1110 1101 would be 
# converted to 1110 0000.

# Task 5-> As illustrated in the image below, split the RGB channels of the  
# rgb.png image , producing three images: R, G, and B, from the original image. 
# As shown in the example below, the pixels (i, j) in image R should represent a shade of red equal to the R component of the pixels (i, j) in the original image. Likewise, images G and B should contain the green and blue intensities of the pixels in the original image.

def criarImagemRGB():
    img = Image.new( "RGB", (512,256))
    raster = img.load()
        
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i,j] = (220,219,97,255)
            
    # obtendo o pixel 0,0
    (r, g, b) = img.getpixel((0, 0))
    print("Pixel (0,0) com getpixel:", r, g, b)
    
    # outra forma
    print("Pixel (0,0): com raster", raster[0, 0])
    
    return img

def criarImagemCinza():
    img = Image.new( "L", (256,256))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            raster[i,j] = i
    y = img.getpixel((5, 5))
    print(y)
    return img

def criarImagemBinaria():
    # checkerboard pattern.
    img = Image.new("1", (500,500))
    raster = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if ((int(i/50)+int(j/50)) % 2 == 0):
                raster[i,j] = 0
            else:
                raster[i,j] = 1
    y = img.getpixel((0, 0))
    print(y)
    return img

img = Image.open(urlopen("https://www.inf.ufsc.br/~roberto.willrich/INE5431/RGB.png"))
print("Largura:", img.width, "Altura:", img.height)
img.show()
criarImagemRGB().show()
criarImagemCinza().show()
criarImagemBinaria().show()
reduceResolution(img).show()
grayScale(img).show()
blackAndWhite(img).show()

