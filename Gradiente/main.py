# from PIL import Image # PIL não estava dando certo, vamos de OpenCV
import cv2, numpy, math

def mediana(list:list):
    # mediana é o elemento no meio de uma lista ordenada de números
    list = sorted(list)
    n = len(list)
    if n % 2 == 0:
        return (int(list[n//2])+int(list[int(n//2)-1]))//2
    return list[n//2]

def is_valid(x, y, size):
    return x >= 0 and y >= 0 and x < size[1] and y < size[0]

def operadores(type:int):
    # retorna os pares de filtros de Sobel, Prewitt e Scharr
    if type == 0: # Sobel
        OX = numpy.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ])
        OY = numpy.array([
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
        ])
    elif type == 1: # Prewitt
        OX = numpy.array([
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]
        ])
        OY = numpy.array([
            [-1, -1, -1],
            [0, 0, 0],
            [1, 1, 1]
        ])
    else: # Scharr
        OX = numpy.array([
            [-3, 0, 3],
            [-10, 0, 10],
            [-3, 0, 3]
        ])
        OY = numpy.array([
            [-3, -10, -3],
            [0, 0, 0],
            [3, 10, 3]
        ])
    return (OX, OY)

def copy_matrix(orig, dest, tamanho):
    # dest tem que ser maior ou igual à orig
    for i in range(tamanho[1]):
        for j in range(tamanho[0]):
            dest[i][j] = orig[i][j]

def filtro_passa_baixa(img, tamanho:tuple):
    tempImg = img.copy() # copiando a img pra não alterar direto na original
    # mudar a original da resultados esquisitos

    for x in range(tamanho[1]):
        for y in range(tamanho[0]):
            vizinhos = []
            for i in range(-1,2):
                for j in range(-1,2):
                    if is_valid(x+i, y+j, tamanho):
                        vizinhos.append(img[x+i][y+j])
            tempImg[x][y] = mediana(vizinhos)
    return tempImg

def filtro_derivativo(img, tamanho:tuple, operador:int):
    tempImg = numpy.zeros(shape=(tamanho[1]+2, tamanho[0]+2))
    # tenho que criar uma cópia da imagem levemente maior que a original
    copy_matrix(img, tempImg, tamanho)

    OX, OY = operadores(operador)
    GX, GY = img.copy(), img.copy()
    for x in range(tamanho[1]):
        for y in range(tamanho[0]):
            janela = tempImg[x:x+3, y:y+3] # sintaxe estranha mais isso faz um recorte 3x3 da img
            GX[x][y] = numpy.absolute(numpy.sum(numpy.matmul(OX, janela)))
            GY[x][y] = numpy.absolute(numpy.sum(numpy.matmul(OY, janela)))
            # absolute == sqrt(a² + b²)
            # sum == somatório dos elementos das matrizes
            # matmul == multiplicação de matrizes
    return (GX, GY)

def magnitude_gradiente(img, tamanho:tuple, componentes:tuple):
    tempImg = img.copy()

    GX, GY = componentes
    for x in range(tamanho[1]):
        for y in range(tamanho[0]):
            tempImg[x][y] = numpy.absolute(GX[x][y] + GY[x][y])
    
    return tempImg

def direcao_gradiente(img, tamanho:tuple, componentes:tuple):
    tempImg = img.copy()

    e = 10**-8
    GX, GY = componentes
    for x in range(tamanho[1]):
        for y in range(tamanho[0]):
            tempImg[x][y] = math.degrees(math.atan2(GY[x][y], GX[x][y]+e))
    
    return tempImg

def filtro_passa_alta(img, tamanho:tuple, k):
    tempImg = img.copy()

    for x in range(tamanho[1]):
        for y in range(tamanho[0]):
            tempImg[x][y] = numpy.uint8(min(255, tempImg[x][y] + k*tempImg[x][y]))

    return tempImg

def main():
    imagens = ["Lua.jpg", "Chess.png", "Egg.jpg"]
    pathIn  = "/home/miguel/Documents/Matérias/PIM/Gradiente/Imagens/"
    pathOut = "/home/miguel/Documents/Matérias/PIM/Gradiente/Resultados/"


    for imagem in imagens:
        img = cv2.imread(pathIn+imagem, 2)
        size = (len(img[0]), len(img))
        # cv2.imshow(imagem, img)
        # input()

        imgPassaBaixa = filtro_passa_baixa(img, size)
        cv2.imwrite(pathOut+"PassaBaixa"+imagem, imgPassaBaixa)

        # Item A da Tarefa
        GXSobel,   GYSobel   = filtro_derivativo(imgPassaBaixa, size, 0)
        cv2.imwrite(pathOut+"GXSobel"+imagem,GXSobel)
        cv2.imwrite(pathOut+"GYSobel"+imagem,GYSobel)

        GXPrewitt, GYPrewitt = filtro_derivativo(imgPassaBaixa, size, 1)
        cv2.imwrite(pathOut+"GXPrewitt"+imagem,GXPrewitt)
        cv2.imwrite(pathOut+"GYPrewitt"+imagem,GYPrewitt)

        GXScharr,  GYScharr  = filtro_derivativo(imgPassaBaixa, size, 2)
        cv2.imwrite(pathOut+"GXScharr"+imagem,GXScharr)
        cv2.imwrite(pathOut+"GYScharr"+imagem,GYScharr)

        # Item B da Tarefa
        imgPassaAlta05 = filtro_passa_alta(img, size, 0.5)
        cv2.imwrite(pathOut+"PassaAlta05"+imagem, imgPassaAlta05)
        imgPassaAlta1  = filtro_passa_alta(img, size, 1)
        cv2.imwrite(pathOut+"PassaAlta1"+imagem, imgPassaAlta1)
        imgPassaAlta15 = filtro_passa_alta(img, size, 1.5)
        cv2.imwrite(pathOut+"PassaAlta15"+imagem, imgPassaAlta15)

if __name__ == "__main__":
    main()