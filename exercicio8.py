#Faça um programa que busca uma matriz dentro de uma outra matriz maior e retorna uma 
#lista com todas as ocorrências
#A primeira linha é um par de números inteiros que representa o tamanho em quantidade 
#de linhas e colunas da matriz que será reazliada a busca (maior)
#As linhas subsequentes (quantidade de linhas definida no item acima) contém os 
#valores desta matriz.
#Após a leitura da primeira matriz, o mesmo processo se repete para definir a segunda
#matriz (menor) que será utilizada como padrão de busca na matriz anterior, ou seja, 
#uma linha com um par de inteiros contendo a quantiade de linhas e colunas seguido 
#por linhas que representam os valores da respectiva matriz.
#Considere todos os números lidos como números inteiros.

def gerar_matriz(linha):
  matriz = list()
  for i in range(linha):
    lin = list()
    for j in input().split():
      lin.append(int(j))
    matriz.append(lin)
  return matriz

def gerar_lista_matriz(matriz_maior, matriz_menor):
  lin_maior, col_maior = len(matriz_maior), len(matriz_maior[0])
  lin_menor, col_menor = len(matriz_menor), len(matriz_menor[0])

  lista_matriz = list()

  for i in range(lin_maior - lin_menor + 1):
    for j in range(col_maior - col_menor + 1):
      submatriz = list()

      for linha in matriz_maior[i:i + lin_menor]:
        submatriz.append(linha[j:j + col_menor])
      lista_matriz.append((submatriz, i, j))
  return lista_matriz

lista1 = input().split()
linha1, coluna1 = int(lista1[0]), int(lista1[1])
matriz1 = gerar_matriz(linha1)

lista2 = input().split()
linha2, coluna2 = int(lista2[0]), int(lista2[1])
matriz2 = gerar_matriz(linha2)

resultado = list()
for submatriz, i, j in gerar_lista_matriz(matriz1, matriz2):
  if submatriz == matriz2:

    resultado.append([i, j])

print(resultado)