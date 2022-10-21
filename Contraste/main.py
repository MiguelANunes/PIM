import cv2, numpy, math#, skimage
from matplotlib import pyplot as plt

pathIn  = "/home/miguel/Documents/Matérias/PIM/Contraste/Imagens/"
pathOut = "/home/miguel/Documents/Matérias/PIM/Contraste/Resultados/"

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
        string = pathOut+"Histograma"+imagem
        print(f"Histograma de {imagem} salvo em {string}")

def item2():
    imagens = ["Clara.jpg", "Escura.jpg", "Marilyn.jpg"]
    for imagem in imagens:
        img = cv2.imread(pathIn+imagem, 2)
        pass

def item3():
    imagem = "Outono"
    pass

def main():
    item1()
    item2()
    item3()

if __name__ == "__main__":
    main()
