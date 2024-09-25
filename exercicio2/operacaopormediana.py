import numpy as np
from PIL import Image
from PIL import ImageFilter
from scipy.ndimage import generic_filter
import	cv2 as cv

# from funcoes.plots import plotaImagemDeArray


import matplotlib.pyplot as plt

# Funcionamento do Main:
#   Mudar a variável enderecoImagem para alterar a imagem a ser modificada
#   Descomentar ou comentar as funções para rodar somente as funções desejadas
def main():
    # Usar '.\*.tif' no windows e './../*.tif' no Linux
    enderecoImagem = '.\lena_gray_512_salt_pepper.tif'
    imagem = Image.open(enderecoImagem)
    # filtroMedia(imagem, 2)
    # filtroMediaPillow(imagem, 3)
    # filtroMediaScipy(imagem, 3)
    # filtroMediaOpenCV(enderecoImagem, 3)
    # filtroMediana(imagem, 2)
    # filtroMedianaPillow(imagem, 3)
    # filtroMedianaScipy(imagem, 3)
    # filtroMedianaOpenCV(enderecoImagem, 3)

# FILTROS USANDO A MÉDIA    

def filtroMedia(img, tam):
    imagemArray = np.array(img)
    imagemFiltro = np.empty(imagemArray.shape)
    [xSize, ySize] = imagemArray.shape
    for x in range(1, xSize - tam):
        for y in range(1, ySize - tam):
            w = imagemArray[x - 1:x + tam, y - 1:y + tam]
            imagemFiltro[x, y] = np.mean(w).astype(int)

    imagemArray = np.array(img)
    plotaImagemDeArray(imagemArray, imagemFiltro)

def filtroMediaPillow(img, tam):
    imagemFiltrada = img.filter(ImageFilter.BoxBlur(tam))
    img.show()
    imagemFiltrada.show()

def filtroMediaScipy(img, tam):
    imagemArray = np.array(img)
    imagemFiltrada = generic_filter(img, np.mean, [tam, tam])
    plotaImagemDeArray(imagemArray, imagemFiltrada)

def filtroMediaOpenCV(endereco, tam):
    img = cv.imread(endereco)
    imagemFiltrada = cv.blur(img, (tam, tam))
    plotaImagemDeArray(img, imagemFiltrada)

# FILTROS USANDO A MEDIANA

def filtroMediana(img, tam):
    imagemArray = np.array(img)
    imagemFiltro = np.empty(imagemArray.shape)
    [xSize, ySize] = imagemArray.shape
    for x in range(1, xSize - tam):
        for y in range(1, ySize - tam):
            w = imagemArray[x - 1:x + tam, y - 1:y + tam]
            imagemFiltro[x, y] = np.median(w).astype(int)

    imagemArray = np.array(img)
    plotaImagemDeArray(imagemArray, imagemFiltro)

def filtroMedianaPillow(img, tam):
    imagemFiltrada = img.filter(ImageFilter.MedianFilter(tam))
    img.show()
    imagemFiltrada.show()

def filtroMedianaScipy(img, tam):
    imagemArray = np.array(img)
    imagemFiltrada = generic_filter(img, np.median, [tam, tam])
    plotaImagemDeArray(imagemArray, imagemFiltrada)

def filtroMedianaOpenCV(endereco, tam):
    img = cv.imread(endereco)
    imagemFiltrada = cv.medianBlur(img, tam)
    plotaImagemDeArray(img, imagemFiltrada)


def plotaImagemDeArray(array, array2):
  imgAntiga = Image.fromarray(array)
  imgNova = Image.fromarray(array2)
  fig, ax = plt.subplots(nrows=1, ncols=2)
  ax[0].imshow(imgAntiga, cmap='gray')
  ax[0].set_title("Imagem original")
  ax[1].imshow(imgNova, cmap='gray')
  ax[1].set_title("Imagem filtrada")
  plt.show()

if __name__ == "__main__":
    main()