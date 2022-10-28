import cv2, skimage, math, numpy
from matplotlib import pyplot as plt
from skimage.io import imread, imshow
from skimage.color import rgb2hsv, rgb2gray, rgb2yuv
from skimage import color, exposure, transform
from skimage.exposure import equalize_hist

pathIn  = "/home/miguel/Documents/Matérias/PIM/Trab 4 Frequencia/Imagens/"
pathOut = "/home/miguel/Documents/Matérias/PIM/Trab 4 Frequencia/Resultados/"

def intensidade(img):
    intensidade = [0] * 256
    for l in img:
        for p in l:
            intensidade[p] += 1
    return intensidade

def probabilidade(arr, h, w):
    p = []
    for j in range(256):
        p.append(arr[j]/(h*w))
    return p

def media(img):
    p = probabilidade(intensidade(img), len(img), len(img[0]))
    media = 0
    for i in range(256):
        media += i * p[i]
    return media

def variancia(img):
    m = media(img)
    p = probabilidade(intensidade(img), len(img), len(img[0]))
    variancia = 0
    for i in range(256):
        variancia += ((i - m)**2) * p[i]
    return variancia

def entropia(img):
    p = probabilidade(intensidade(img), len(img), len(img[0]))
    entropia = 0
    for i in range(256):
        if p[i] == 0: 
            continue
        entropia -= p[i] * math.log2(p[i])
    return entropia

def histograma(img, nome):
    plt.hist(img.ravel(), 256, [0,256])
    plt.savefig(pathOut+"Histograma"+nome)
    plt.close()

def equalizar(img):
    imagem_yuv = skimage.color.rgb2yiq(img.rgb)
    imagem_yuv[:,:,0] = cv2.equalizeHist(imagem_yuv[:,:,0])
    img_equalizada = skimage.color.yiq2rgb(img.yiq)

    return img_equalizada

def item1():
    imagens = ["Clara.jpg", "Escura.jpg", "Lena.png"]

    for imagem in imagens:
        img = cv2.imread(pathIn+imagem, 2)

        m = media(img)
        print(f"Media de {imagem}: {m}")

        v = variancia(img)
        print(f"Variância de {imagem}: {v}")

        e = entropia(img)
        print(f"Entropia de {imagem}: {e}")

        histograma(img, imagem)
        string = "Item1"+pathOut+"Histograma"+imagem
        print(f"Item 1 - Histograma de {str(imagem)} salvo em {string}")

def fourier():
    imagens = ["Folhas.jpg"]

    for imagem in imagens:
        img = cv2.imread(pathIn+imagem, 2)

        imgFourier = numpy.fft.fftshift(numpy.fft.fft2(img))
        plt.figure(num=None, figsize=(8, 6), dpi=80)
        plt.imshow(numpy.log(abs(imgFourier)), cmap='gray');

def main():
    fourier()

if __name__ == "__main__":
    main()