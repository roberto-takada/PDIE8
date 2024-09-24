import numpy as np
from PIL import Image

from funcoes.plots import plotaImagemDeArray


def main():
    enderecoImagem = './../lena_gray_512_salt_pepper.tif'
    imagem = Image.open(enderecoImagem)
    # filtroMedia(imagem, 3)
    filtroMediana(imagem, 3)


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

if __name__ == "__main__":
    main()