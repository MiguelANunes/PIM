from PIL import Image

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
        
        vizinhos = []
        for move in moves:
            # carregando todos os vizinhos do pixel atual
            x,y = move[0]+prox[0], move[1]+prox[1]

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

def find_conexos(imagem, pixels):
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

moedas = Image.open("Moedas2.jpg").convert("L")
pixels = moedas.load() # pixels é a matriz de pixels da imagem, não posso acessar isso de outra forma
# moedas.save("Moedas2Cinzas.png")
# exit()
razao = 27/20 # moeda de R$1 tem 27 mm de diâmetro, R$0,10 tem 20 mm de diâmetro
print(razao)
limiar = (25,200)
aplica_limiar(moedas, pixels, limiar)
moedas.show()
encontradas = find_conexos(moedas, pixels)
# lista de listas de pares (x,y) de pixels que compõe moedas

# criando uma nova imagem que tem todas as moedas da imagem original pintadas de vemelho
moedasVermelhas = Image.new("RGB", moedas.size)
pixelsVermelhos = moedasVermelhas.load()
popula_imagem(pixelsVermelhos, encontradas)
moedasVermelhas.save("Moedas2Vermelhas")