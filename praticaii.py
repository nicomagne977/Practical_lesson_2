from urllib.request import urlopen
from PIL import Image # package pillow
import math

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


#Task 5 
def separarCanais():
    img = Image.open("rgb.png")
    img_R = Image.new("RGB", img.size)
    img_B = Image.new("RGB", img.size)
    img_G = Image.new("RGB", img.size)
    raster = img.load()
    raster_R = img_R.load()
    raster_B = img_B.load() 
    raster_G = img_G.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            (r,g,b,_) = img.getpixel((i,j))
            raster_R[i,j] = (r,0,0,_)
            raster_G[i,j] = (0,g,0,_)
            raster_B[i,j] = (0,0,b,_)
    img_R.show()
    img_G.show()
    img_B.show()
    return img_R, img_G, img_B

separarCanais()

