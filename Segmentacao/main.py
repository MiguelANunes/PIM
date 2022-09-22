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

moedas = Image.open("Moedas.png").convert("L")
pixels = moedas.load()
# moedas.save("MoedasCinzas.png")
razao = 27/20 # moeda de R$1 tem 27 mm de diâmetro, R$0,10 tem 20 mm de diâmetro
limiar = (0,130)
aplica_limiar(moedas, pixels, limiar)
moedas.show()