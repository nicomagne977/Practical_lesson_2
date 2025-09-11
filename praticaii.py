from urllib.request import urlopen
from PIL import Image # package pillow
import math

# Task 1 -> Reduce the resolution of the image to half the height 
# and width of the  rgb.png  image and display this image.


# Task 2 -> Convert rgb.png image to grayscale and display it.

# Task 3-> Transform rgb.png image   into binary image and display it.

# Task 4-> Reduce the number of bits per pixel of the rgb.png image to 3 bits. 
# Tip: To do this, perform a binary operation to keep only the 3 most significant 
# bits of each color component. For example, an R channel of 1110 1101 would be 
# converted to 1110 0000.

# Task 5-> As illustrated in the image below, split the RGB channels of the  
# rgb.png image , producing three images: R, G, and B, from the original image. 
# As shown in the example below, the pixels (i, j) in image R should represent a 
# shade of red equal to the R component of the pixels (i, j) in the original image. Likewise, 
# images G and B should contain the green and blue intensities of the pixels in the original image.

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

def reduzirPara3Bits(img):
    """
    Task 4: Reduce the number of bits per pixel to 3 bits by keeping only 
    the 3 most significant bits of each color component.
    """
    # Create a copy of the image to work with
    img_3bits = img.copy()
    raster = img_3bits.load()
    
    # Process each pixel
    for i in range(img_3bits.size[0]):
        for j in range(img_3bits.size[1]):
            # Get the original RGB values
            r, g, b = img.getpixel((i, j))
            
            # Keep only the 3 most significant bits for each component
            # This is done by shifting right by 5 bits (8-3=5) and then left by 5 bits
            # This effectively zeros out the 5 least significant bits
            r_3bits = (r >> 5) << 5
            g_3bits = (g >> 5) << 5
            b_3bits = (b >> 5) << 5
            
            # Set the new pixel value
            raster[i, j] = (r_3bits, g_3bits, b_3bits)
    
    return img_3bits

img = Image.open(urlopen("https://www.inf.ufsc.br/~roberto.willrich/INE5431/RGB.png"))
print("Largura:", img.width, "Altura:", img.height)
img.show()
criarImagemRGB().show()
criarImagemCinza().show()
criarImagemBinaria().show()

# Task 4: Reduce image to 3 bits per pixel
print("Task 4: Reducing image to 3 bits per pixel...")
img_3bits = reduzirPara3Bits(img)
img_3bits.show()

