import cv2, skimage
from matplotlib import pyplot as plt
 
imagem1 = cv2.imread('Imagens/Outono.png')
pathOut = "D:/Documentos/Code/UDESC/PIM/Contraste/Resultados/"

def histograma(img, nome):
    plt.hist(img.ravel(), 256, [0,256])
    plt.savefig(pathOut+"Histograma"+nome)
    plt.close()

imagem_yuv = skimage.color.rgb2yiq(imagem1)
ok = histograma(imagem_yuv, "OUTONO PRE.png")
imagem_yuv[:,:,0] = cv2.equalizeHist(imagem_yuv[:,:,0])
img_equalizada = skimage.color.yiq2rgb(imagem_yuv)
iguess = histograma(img_equalizada, "OUTONO POS.png")
print(iguess)

cv2.imwrite('{imagem1}.jpg', img_equalizada)