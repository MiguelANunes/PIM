import cv2
from matplotlib import pyplot as plt
 
imagem1 = cv2.imread('Imagens/Outono.png')
pathOut = "D:/Documentos/Code/UDESC/PIM/Contraste/Item3/"

def histograma(img, nome):
    plt.hist(img.ravel(), 256, [0,256])
    plt.savefig(pathOut+"Histograma"+nome)
    plt.close()

imagem_yuv = cv2.cvtColor(imagem1,cv2.COLOR_BGR2YUV)
histograma(imagem_yuv, "RGB_PRA_YUV.png")
imagem_yuv[:,:,0] = cv2.equalizeHist(imagem_yuv[:,:,0])
img_equalizada = cv2.cvtColor(imagem_yuv, cv2.COLOR_YUV2BGR)
plt.hist1(img_equalizada.ravel(), 256, [0,256])

cv2.imwrite('{imagem1}.jpg', img_equalizada)