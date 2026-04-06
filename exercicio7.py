#Faça um programa que cria duas matrizes aleatórias e imprima o resultado da 
#multiplicação delas.
#O primeiro argumento é o valor inicial do random.seed. Este valor é do tipo inteiro, 
#e é preciso convertê-lo usando int(input())).
#A segunda linha contém informações para gerar a primeira matriz, e contém quatro 
#parâmetros: a linha, a coluna, o menor valor aleatório (incluso) e o maior valor 
#aleatório (incluso).
#IMPORTANTE: utilize a função random.randint(min,max) para sortear os valores da 
#matriz, seguindo a sequência de linhas.
#A terceira linha é igual à segunda linha, mas com informações para gerar a segunda matriz.

import random

def gerar_matriz(linha, coluna, minimo, maximo):
  matriz = list()
  for i in range(linha):
    lin = list()
    for j in range(coluna):
      lin.append(random.randint(minimo, maximo))
    matriz.append(lin)
  return matriz

def matriz_zeros(linha, coluna):
  matriz = list()
  for i in range(linha):
    matriz.append([0]*coluna)
  return matriz

seed = int(input())
random.seed(seed)

lista1 = input().split()
linha1, coluna1, min1, max1 = int(lista1[0]), int(lista1[1]), int(lista1[2]), int(lista1[3])

lista2 = input().split()
linha2, coluna2, min2, max2 = int(lista2[0]), int(lista2[1]), int(lista2[2]), int(lista2[3])

matriz1 = gerar_matriz(linha1, coluna1, min1, max1)
matriz2 = gerar_matriz(linha2, coluna2, min2, max2)
matriz_final = matriz_zeros(linha1, coluna2)

if coluna1 != linha2:
  print("Matrizes incompatíveis")

else:
  for i in range(linha1):
    for j in range(coluna2):
      for k in range(coluna1):
        matriz_final[i][j] += matriz1[i][k] * matriz2[k][j]
  for linha in matriz_final:
    print(linha)