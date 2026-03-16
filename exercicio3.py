# Leia todas as notas (quantidade definido em tamanho);
# Calcule a média de todas as notas;
# Calcule uma nova média considerando apenas as notas acima da média. Desconsiderar as notas iguais a média;
# Imprima a média acima da média.

import numpy as np # type: ignore

tamanho = int(input())
notas = np.zeros(tamanho)

for i in range(0, tamanho):
  notas[i] = float(input())

def calculo_media(notas):
  soma = 0
  for i in notas:
    soma += i
  return soma/len(notas)

def media_das_notas_acima_da_media(notas):
  soma = 0
  quantidade = 0
  for i in notas:
    if i > calculo_media(notas):
      soma += i
      quantidade += 1
  return soma/quantidade

print(media_das_notas_acima_da_media(notas))