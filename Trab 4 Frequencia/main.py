import cv2, skimage, math, numpy
from matplotlib import pyplot as plt
from skimage.io import imread, imshow
from copy import copy, deepcopy

pathIn  = "/home/miguel/Documents/Matérias/PIM/Trab 4 Frequencia/Imagens/"
pathOut = "/home/miguel/Documents/Matérias/PIM/Trab 4 Frequencia/Resultados/"

def fourier_mascara_horizontal(img, mascara):
    img[235:240, :230] = mascara
    img[235:240,-230:] = mascara
    return img

def fourier_mascara_vertical(img, mascara):
    img[:225, 235:240] = mascara
    img[-225:,235:240] = mascara
    return img

def fourier(mascara):
    imagens = ["Folhas.jpg"]

    for imagem in imagens:
        img = imread(pathIn+imagem)

        imgFourier    = numpy.fft.fftshift(numpy.fft.fft2(img))
        # imgFourierHor = fourier_mascara_horizontal(copy(imgFourier), mascara)
        # imgFourierVer = fourier_mascara_vertical(copy(imgFourier), mascara)
        # imgFourierHorVer = fourier_mascara_horizontal(fourier_mascara_vertical(copy(imgFourier), mascara), mascara)

        imgTransformada = abs(numpy.fft.ifft2(fourier_mascara_horizontal(fourier_mascara_vertical(imgFourier, mascara), mascara))) 
        plt.figure(num=None, figsize=(8, 6), dpi=80)
        plt.imshow(imgTransformada, cmap='gray');
        plt.show()

def main():
    fourier(0)

if __name__ == "__main__":
    main()