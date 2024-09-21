import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def main():
  enderecoImagem = './house.tif'
  img = Image.open(enderecoImagem)
  print('INFO IMAGEM')
  print(img.format)
  print(img.size)
  print(img.mode)
  transformaNegativo(img)
  # divideMetade(img)
  # adicionaQuadrados(img)
  # adicionaQuadradoPreto(img)

# Adiciona um quadrado preto no centro da imagem
def adicionaQuadradoPreto(img):
  npImagem = np.array(img)
  npImagemQuadradoPreto = np.array(img)
  [xMax,yMax] = img.size
  xMedia = int(xMax / 2)
  yMedia = int(yMax / 2)
  size = 15
  sizeDiv2 = int(size / 2)
  xMediaStart = xMedia - sizeDiv2
  yMediaStart = yMedia - sizeDiv2
  npImagemQuadradoPreto[xMediaStart:xMediaStart+size, yMediaStart:yMediaStart+size] = 0
  plotImageDeArray(npImagem, npImagemQuadradoPreto)

# Adiciona quatro quadrados brancos nos quatro quantos da imagem, não utilizar valor quebrado em size
def adicionaQuadrados(img):
  npImagem = np.array(img)
  npImagemQuadrados = np.array(img)
  [xMax,yMax] = img.size
  xIni = 0
  yIni = 0
  size = 10
  npImagemQuadrados[xIni:xIni+size,yIni:yIni+size] = 255
  npImagemQuadrados[xIni:xIni+size,yMax-size:yMax] = 255
  npImagemQuadrados[xMax-size:xMax,yIni: yIni+size] = 255
  npImagemQuadrados[xMax-size:xMax,yMax-size:yMax] = 255
  plotImageDeArray(npImagem, npImagemQuadrados)

# Divide o valor da escala cinza pela metade
def divideMetade(img):
  npImagem = np.array(img)
  npImagemMetade = np.array(img)
  npImagemMetade = npImagem / 2
  plotImageDeArray(npImagem, npImagemMetade)

# Deixa a imagem negativada
def transformaNegativo(img):
  npImagem = np.array(img)
  npImagemNegativo = npImagem
  npImagemNegativo = 255 - npImagem
  plotImageDeArray(npImagem, npImagemNegativo)

# Usar para mostrar um array 10x10 da escala de cor
def plotArray10x10(array):
  print(array[0:10,0:10])

# Plota a imagem a partir de um array
def plotImageDeArray(array, array2):
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