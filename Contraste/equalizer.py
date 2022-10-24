import cv2
import numpy
 
imagem1 = cv2.imread('Imagens/Outono.png')

imagem_yuv = cv2.cvtColor(imagem1,cv2.COLOR_BGR2YUV)
imagem_yuv[:,:,0] = cv2.equalizeHist(imagem_yuv[:,:,0])
img_equalizada = cv2.cvtColor(imagem_yuv, cv2.COLOR_YUV2BGR)

cv2.imwrite('{imagem1}.jpg', img_equalizada)