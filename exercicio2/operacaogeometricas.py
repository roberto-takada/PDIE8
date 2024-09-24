import numpy as np
from PIL import Image
from scipy import ndimage

from funcoes.plots import plotaImagemDeArray

# Funcionamento do Main:
#   Mudar a variável enderecoImagem para alterar a imagem a ser modificada
#   Descomentar ou comentar as funções para rodar somente as funções desejadas
def main():
    enderecoImagem = './../house.tif'
    imagem = Image.open(enderecoImagem)
    # rotacaoNGraus(imagem, 45)
    # zoomInEOut(imagem, 10)
    translacaoXeY(imagem, 45, 70)

def zoomInEOut(img, zoom):
    imagemArray = np.array(img)
    imagemZoom = ndimage.zoom(imagemArray, zoom)
    imagemArray = np.array(img)
    plotaImagemDeArray(imagemArray, imagemZoom)

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


if __name__ == "__main__":
    main()