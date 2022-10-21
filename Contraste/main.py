import cv2, numpy, math, skimage

pathIn  = "/home/miguel/Documents/Matérias/PIM/Contraste/Imagens/"
pathOut = "/home/miguel/Documents/Matérias/PIM/Contraste/Resultados/"

def entropia(img):
    intensidade = [0] * 256
    for linha in img:
        pass

def item1():
    imagens = ["Clara.jpg", "Escura.jpg", "Lena.png"]
    for imagem in imagens:
        img = cv2.imread(pathIn+imagem, 2)
        entropia = entropia(img)

def item2():
    imagens = ["Clara.jpg", "Escura.jpg", "Marilyn.jpg"]
    for imagem in imagens:
        pass

def item3():
    imagem = "Outono"
    pass

def main():

    item1()
    item2()
    item3()
    # for imagem in imagens:
    #     img = cv2.imread(pathIn+imagem, 2)
    #     size = (len(img[0]), len(img))
    #     # cv2.imshow(imagem, img)
    #     # input()

    #     imgPassaBaixa = filtro_passa_baixa(img, size)
    #     cv2.imwrite(pathOut+"PassaBaixa"+imagem, imgPassaBaixa)

    #     # Item A da Tarefa
    #     GXSobel,   GYSobel   = filtro_derivativo(imgPassaBaixa, size, 0)
    #     cv2.imwrite(pathOut+"GXSobel"+imagem,GXSobel)
    #     cv2.imwrite(pathOut+"GYSobel"+imagem,GYSobel)

    #     GXPrewitt, GYPrewitt = filtro_derivativo(imgPassaBaixa, size, 1)
    #     cv2.imwrite(pathOut+"GXPrewitt"+imagem,GXPrewitt)
    #     cv2.imwrite(pathOut+"GYPrewitt"+imagem,GYPrewitt)

    #     GXScharr,  GYScharr  = filtro_derivativo(imgPassaBaixa, size, 2)
    #     cv2.imwrite(pathOut+"GXScharr"+imagem,GXScharr)
    #     cv2.imwrite(pathOut+"GYScharr"+imagem,GYScharr)

    #     # Item B da Tarefa
    #     imgPassaAlta05 = filtro_passa_alta(img, size, 0.5)
    #     cv2.imwrite(pathOut+"PassaAlta05"+imagem, imgPassaAlta05)
    #     imgPassaAlta1  = filtro_passa_alta(img, size, 1)
    #     cv2.imwrite(pathOut+"PassaAlta1"+imagem, imgPassaAlta1)
    #     imgPassaAlta15 = filtro_passa_alta(img, size, 1.5)
    #     cv2.imwrite(pathOut+"PassaAlta15"+imagem, imgPassaAlta15)

if __name__ == "__main__":
    main()