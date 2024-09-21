import matplotlib.pyplot as plt
from PIL import Image

# Plota a imagem a partir de um array
def plotaImagemDeArray(array, array2):
  imgAntiga = Image.fromarray(array)
  imgNova = Image.fromarray(array2)
  fig, ax = plt.subplots(nrows=1, ncols=2)
  ax[0].imshow(imgAntiga, cmap='gray')
  ax[0].set_title("Imagem original")
  ax[1].imshow(imgNova, cmap='gray')
  ax[1].set_title("Imagem filtrada")
  plt.show()