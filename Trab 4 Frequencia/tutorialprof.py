import cv2
import numpy as np
import matplotlib.pyplot as plt

dark_image = cv2.imread("Imagens/Folhas.jpg", 0)

dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(dark_image))
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')


def fourier_masker_ver(image, i):
    f_size = 15
    dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(image))
    dark_image_grey_fourier[:225, 235:240] = i
    dark_image_grey_fourier[-225:, 235:240] = i
    fig, ax = plt.subplots(1, 2, figsize=(15, 15))
    ax[0].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')
    ax[0].set_title('Masked Fourier', fontsize=f_size)
    ax[1].imshow(abs(np.fft.ifft2(dark_image_grey_fourier)),
                 cmap='gray')
    ax[1].set_title('Transformed Greyscale Image',
                    fontsize=f_size)


def fourier_masker_hor(image, i):
    f_size = 15
    dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(image))
    dark_image_grey_fourier[235:240, :230] = i
    dark_image_grey_fourier[235:240, -230:] = i
    fig, ax = plt.subplots(1, 2, figsize=(15, 15))
    ax[0].imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray')
    ax[0].set_title('Masked Fourier', fontsize=f_size)
    ax[1].imshow(abs(np.fft.ifft2(dark_image_grey_fourier)),
                 cmap='gray')
    ax[1].set_title('Transformed Greyscale Image',
                    fontsize=f_size)


def fourier_iterator(image, value_list):
    for i in value_list:
        img_ver = fourier_masker_ver(image, i)
        img_hor = fourier_masker_hor(img_ver, i)


fourier_masker_ver(dark_image, 1)
fourier_masker_hor(dark_image, 1)
fourier_iterator(dark_image, [0, 1, 100])
plt.show()
