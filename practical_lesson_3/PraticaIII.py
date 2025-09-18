from PIL import Image
from Cuif import Cuif
import math


def PSNR(original, decodificada, b):
    try:
        mse = MSE(original, decodificada)
        psnr = 10 * math.log10(((2**b - 1) ** 2) / mse)
        return psnr
    except ZeroDivisionError:
        return "Infinito"


def MSE(ori, dec):
    nsymbols = ori.width * ori.height * 3
    for i in range(ori.width):
        for j in range(ori.height):
            ori_r, ori_g, ori_b = ori.getpixel((i, j))
            dec_r, dec_g, dec_b = dec.getpixel((i, j))
    return 0


if __name__ == "__main__":
    filepath = "lena.bmp"
    img = Image.open(filepath)
    matriculas = [23100481, 945542, 202503768]

    # instancia objeto Cuif, convertendo imagem em CUIF.1
    cuif = Cuif(img, 1, matriculas)

    # imprime cabeçalho Cuif
    cuif.printHeader()

    # gera o arquivo Cuif.1
    cuif.save("lena1.cuif")

    # Abre um arquivo Cuif e gera o objeto Cuif
    # cuif1 = Cuif.openCUIF('lena1.cuif')

    # Converte arquivo Cuif em BMP e mostra
    # cuif1.saveBMP("lena1.bmp")
    # cuif1.show()
    # img1 = Image.open("lena1.bmp")

    # Cálculo do PSNR
    # psnr = PSNR(img, img1, 8)
    # print(f'Cálculo do PSNR: {psnr}')

    # -------- Question 6 ------------#
    # Gera CUIF.1 e BMP correspondente
    cuif1 = Cuif(img, 1, matriculas)
    cuif1.printHeader()
    cuif1.save("lena1.cuif")
    cuif1.saveBMP("lena1.bmp")

    # Gera CUIF.2 e BMP correspondente
    cuif2 = Cuif(img, 2, matriculas)
    cuif2.printHeader()
    cuif2.save("lena2.cuif")
    cuif2.saveBMP("lena2.bmp")

    # Visualiza as imagens geradas
    print("Visualizando lena1.bmp...")
    cuif1.show()
    print("Visualizando lena2.bmp...")
    cuif2.show()

    # Se quiser calcular PSNR entre original e reconstruída:
    # img1 = Image.open('lena1.bmp')
    # img2 = Image.open('lena2.bmp')
    # psnr1 = PSNR(img, img1, 8)
    # psnr2 = PSNR(img, img2, 8)
    # print(f'PSNR lena1.bmp: {psnr1}')
    # print(f'PSNR lena2.bmp: {psnr2}')
