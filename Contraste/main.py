import cv2, skimage, math, numpy
from matplotlib import pyplot as plt

pathIn  = "D:/Documentos/Code/UDESC/PIM/Contraste/Imagens/"
pathOut = "D:/Documentos/Code/UDESC/PIM/Contraste/Resultados/"

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
    img_numpy = numpy.array(img)
    imagem_yuv = cv2.cvtColor(img_numpy,cv2.COLOR_BGR2YUV)
    imagem_yuv[:,:,0] = cv2.equalizeHist(imagem_yuv[:,:,0])
    img_equalizada = cv2.cvtColor(imagem_yuv, cv2.COLOR_YUV2BGR)

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

def item2():
    imagens = ["Clara.jpg", "Escura.jpg", "Marilyn.jpg"]
   
    for imagem in imagens:
        pass
        

def item3():
    imagem = "Outono"

    img = equalizar(imagem)

    cv2.imwrite('{imagem}.jpg', img)

    histograma(img, imagem)
    string = "Item3"+pathOut+"Histograma"+imagem
    print(f"Item 3 - Histograma de {str(imagem)} salvo em {string}")

def main():
    item1()
    item2()
    item3()

if __name__ == "__main__":
    main()
