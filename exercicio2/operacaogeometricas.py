import numpy as np
from PIL import Image
from scipy import ndimage


# from funcoes.plots import plotaImagemDeArray

import matplotlib.pyplot as plt

# Funcionamento do Main:
#   Mudar a variável enderecoImagem para alterar a imagem a ser modificada
#   Descomentar ou comentar as funções para rodar somente as funções desejadas
def main():
    # Usar '.\*.tif' no windows e './../*.tif' no Linux
    enderecoImagem = '.\house.tif'
    imagem = Image.open(enderecoImagem)
    # rotacaoNGraus(imagem, 45)
    # zoomInEOut(imagem, 10)
    # ZoomInEOutSciPy(imagem, 0.5)
    ZoomInEOutNumPy(imagem, 2)
    # translacaoXeY(imagem, 45, 70)
    
def zoomInEOut(img, zoom):
    imagemArray = np.array(img)
    imagemZoom = ndimage.zoom(imagemArray, zoom)
    imagemArray = np.array(img)
    plotaImagemDeArray(imagemArray, imagemZoom)

def ZoomInEOutSciPy(img, zoom):
    imagemArray = np.array(img)
    imagemZoom = ndimage.zoom(imagemArray, zoom)
    plotaImagemDeArray(imagemArray, imagemZoom)

def ZoomInEOutNumPy(img, zoom):
    imagemArray = np.array(img)
    new_img = np.array(img)
    transformacao = [[zoom, 0, 0], [0, zoom, 0], [0, 0, 1]]
    for i in range(len(imagemArray)):
        for j in range(len(transformacao[0])):
            for k in range(len(transformacao)):

                # resulted matrix
                new_img[i][j] += imagemArray[i][k] * transformacao[k][j]

    print(new_img)
    plotaImagemDeArray(imagemArray, new_img)


def rotacaoNGraus(img, graus):
    imagemArray = np.array(img)
    imagemRotacionada = ndimage.rotate(imagemArray, graus, cval=0)
    imagemArray = np.array(img)
    plotaImagemDeArray(imagemArray, imagemRotacionada)


def translacaoXeY(img, x, y):
    imagemArray = np.array(img)
    transform = [[1, 0, y],
                 [0, 1, x],
                 [0, 0, 1]]
    imagemTranslacao = ndimage.affine_transform(imagemArray,
                                              transform)
    plotaImagemDeArray(imagemArray, imagemTranslacao)


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