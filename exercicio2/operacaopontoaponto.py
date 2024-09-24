import numpy as np
from PIL import Image

from funcoes.plots import plotaImagemDeArray


# Funcionamento do Main:
#   Mudar a variável enderecoImagem para alterar a imagem a ser modificada
#   Descomentar ou comentar as funções para rodar somente as funções desejadas
def main():
  enderecoImagem = './../house.tif'
  img = Image.open(enderecoImagem)
  print('INFO IMAGEM')
  print(img.format)
  print(img.size)
  print(img.mode)
  transformaNegativo(img)
  divideMetade(img)
  adicionaQuadrados(img)
  adicionaQuadradoPreto(img)

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
  plotaImagemDeArray(npImagem, npImagemQuadradoPreto)

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
  plotaImagemDeArray(npImagem, npImagemQuadrados)

# Divide o valor da escala cinza pela metade
def divideMetade(img):
  npImagem = np.array(img)
  npImagemMetade = np.array(img)
  npImagemMetade = npImagem / 2
  plotaImagemDeArray(npImagem, npImagemMetade)

# Deixa a imagem negativada
def transformaNegativo(img):
  npImagem = np.array(img)
  npImagemNegativo = npImagem
  npImagemNegativo = 255 - npImagem
  plotaImagemDeArray(npImagem, npImagemNegativo)



if __name__ == "__main__":
  main()    