from PIL import Image

def in_tuple(val:int, t:tuple):
    if val >= t[0] and val <= t[1]:
        return True
    return False

imagem = Image.open("img.jpg")
r, g, b = imagem.getpixel((0,0))
lower = (0, 25)
upper = (230, 255)

if in_tuple(r, upper) and in_tuple(g, upper) and in_tuple(b, upper):
    print("Branco")
    exit()

if in_tuple(r, lower) and in_tuple(g, lower) and in_tuple(b, lower):
    print("Preto")
    exit()

if in_tuple(r, upper):
    print("Vermelho")
    exit()

if in_tuple(g, upper):
    print("Verde")
    exit()

if in_tuple(b, upper):
    print("Azul")
    exit()