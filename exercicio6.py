def matriz_borda_crescente(linhas, comprimento):
  matriz = list()

  for i in range(linhas):
    linha = list()
    for j in range(i, comprimento + i):
      linha.append(j)
    matriz.append(linha)
  return matriz

#Cria uma matriz em que as diagonais estão listadas em ordem crescente.
#Exemplo:
#Entrada: m = 5 e n = 3
#Saída: [ [0, 1, 2],
#         [1, 2, 3],
#         [2, 3, 4],
#         [3, 4, 5],
#         [4, 5, 6] ]

def matriz_simetrica(linhas, comprimento):
  matriz = list()

  for i in range(linhas):
    linha = list()
    for j in range(comprimento):
      if (i - j) >=0:
        linha.append((i - j))
      else:
        linha.append(-(i - j))
    matriz.append(linha)

  return matriz

#Cria uma matriz simétrica.
#Exemplo:
#Entrada: m = 4 e n = 4
#Saída: [ [0, 1, 2, 3],
#         [1, 0, 1, 2],
#         [2, 1, 0, 1],
#         [3, 2, 1, 0] ]

def eh_matriz_quadrada(matriz):
  if not matriz:
    return False

  tamanho = len(matriz[0])

  for linhas in matriz:
    if len(linhas) != tamanho or len(matriz) != len(linhas):
      return False
  return True

#Verifica se M é uma matriz (todas as linhas tem a mesma quantidade de
#elementos) e se é quadrada (a quantidade de linha é a mesma que a coluna).

def eh_diagonal(matriz):
  if not eh_matriz_quadrada(matriz):
    return False

  for i in range(len(matriz)):
    for j in range(len(matriz)):

      if i!=j:
        if matriz[i][j] != 0:
            return False
  return True

#Verifica se uma matriz é quadrada e se os elementos que não pertencem à
#diagonal principal são iguais a zero.

def matriz_transposta(matriz):
  if not matriz:
    return matriz

  nova_matriz = list()

  for i in range(len(matriz[0])):
    linha = list()
    for j in range(len(matriz)):
      linha.append(matriz[j][i])
    nova_matriz.append(linha)

  return nova_matriz

#Retorna a matriz transposta de M.