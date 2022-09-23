from PIL import Image

def in_tuple(val:int, t:tuple):
    if val >= t[0] and val <= t[1]:
        return True
    return False

def aplica_limiar(imagem, pixels, limiar:tuple):
    xsize, ysize = imagem.size

    for i in range(xsize):
        for j in range(ysize):
            if pixels[i,j] >= limiar[0] and pixels[i,j] <= limiar[1]:
                # colorindo como branco todos os pixels que estão dentro do limiar
                pixels[i,j] = 255
            else:
                pixels[i,j] = 0
    
    return pixels

def BFS(imagem, pixels, start):
    xsize, ysize = imagem.size

    moves = [(0,1),(0,2),(1,0),(2,0),(0,-1),(0,-2),(-1,0),(-2,0), (1,1), (1,-1),(-1,-1),(-1,1)]
    # movimento de um BFS em Norte/Sul/Leste/Oeste em 2 níveis

    brancos = [] # lista contendo todos os pixels brancos que encontrei

    # próximos pixels que vou visitar
    visitar = [start]
    visitados = []

    ignorePixel = lambda x,y: x <= 0 or y <= 0 or x >= xsize or y >= ysize or (x,y) in visitados or (x,y) in brancos

    while len(visitar) > 0:
        prox = visitar.pop(0)
        visitados.append(prox)
        
        vizinhos = []
        for move in moves:
            # carregando todos os vizinhos do pixel atual
            x,y = move[0]+prox[0], move[1]+prox[1]
            # print(f"Estou olhando para {(x,y)}")

            if ignorePixel(x,y):
                continue

            vizinhos.append((x,y))
        
        for vizinho in vizinhos:
            vx, vy = vizinho

            if pixels[vx,vy] == 255:
                # se achou um pixel branco, põe na lista e marca pra visitar
                brancos.append(vizinho)
                visitar.append(vizinho)
    return brancos

def ignore_sublist(outerList, item):
    for sublist in outerList:
        if item in sublist:
            return True
    return False

def encontra_moedas(imagem, pixels):
    xsize, ysize = imagem.size

    objetos = []

    print("Estou procurando")
    for i in range(xsize):
        for j in range(ysize):
            if pixels[i,j] == 255 and not ignore_sublist(objetos, (i,j)):
                print("\tIndo para o BFS")
                # BFS para achar todos os pixels brancos conexos com o atual
                objeto = BFS(imagem, pixels, (i,j))
                objetos.append(objeto)
                print(f"\t{len(objeto)}")

    # removendo todos as coisas que encontrou que não são moedas
    objetos = [obj for obj in objetos if len(obj) >= 10000]
    return objetos

def popula_imagem(pixels, pixelsColoridos):
    for objeto in pixelsColoridos:
        for pixel in objeto:
            pixels[pixel[0],pixel[1]] = (255,0,0)

def main():

    # carregando a imagem
    moedas = Image.open("Moedas.jpg").convert("L")
    pixels = moedas.load() # pixels é a matriz de pixels da imagem, não posso acessar isso de outra forma
    # moedas.save("Moedas2Cinzas.png")
    # exit()

    limiar = (25,200)
    aplica_limiar(moedas, pixels, limiar)
    # moedas.show()
    moedasEncontradas = encontra_moedas(moedas, pixels)
    # lista de listas de pares (x,y) de pixels que compõe moedas

    tamanhos = [len(moeda) for moeda in moedasEncontradas]
    tamanhos.sort()
    # gerando uma lista contendo os tamanhos das moedas e ordenando do maior para o menor
    maiorMoeda = max(tamanhos) # pegando a maior moeda

    # moedas de 1 real são maiores que de 10 centavos
    # logo, para filtrar todas as moedas de 1 real, deve selecionar todas as moedas que tem +ou-
    # o mesmo tamanho que a maior moeda
    # toda moeda que não é de 1 real é de 10 centavos

    moedas1Real = []
    moedas10Centavos = []
    for tamanhoMoeda in tamanhos:
        if in_tuple(tamanhoMoeda, (maiorMoeda-((1/10)*tamanhoMoeda), maiorMoeda+((1/10)*tamanhoMoeda))):
            moedas1Real.append(tamanhoMoeda)
        else:
            moedas10Centavos.append(tamanhoMoeda)
    
    valor = len(moedas1Real) + (0.1*len(moedas10Centavos))

    print("Valor total na imagem: R${:.2f}".format(valor))

    # criando uma nova imagem que tem todas as moedas da imagem original pintadas de vermelho
    # moedasVermelhas = Image.new("RGB", moedas.size)
    # pixelsVermelhos = moedasVermelhas.load()
    # popula_imagem(pixelsVermelhos, encontradas)
    # moedasVermelhas.save("Moedas2Vermelhas")

if __name__ == "__main__":
    main()