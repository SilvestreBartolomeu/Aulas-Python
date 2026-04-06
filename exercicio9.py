#Faça um programa que lê um arquivo PGM tipo P2 e retorne um novo arquivo PGM tipo P2 
#com a metade da resolução.

#Na entrada, a primeira linha é o tipo do PGM. No caso, sempre será 'P2', ou seja, tipo texto.
#A segunda linha contem dois inteiros: a quantiade de colunas e a quantiade de linhas da imagem.
#A terceira linha contém o valor máximo que um pixel pode ter, ou seja, cada pixel 
#pode ter um valor entre 0 e o valor máximo definido (inclusive).
#A quarta linha em diante contém uma matriz com as intensidades de cada pixel.
#Considere todos os números lidos como números inteiros, exceto a primeira linha (será sempre 'P2').

#A saida sera um texto que representa uma imagem PGM tipo P2 com as seguintes características:
#Metade da resolução. O novo valor será a soma dos seus vizinhos, ou seja, uma área 
#2x2 (com 4 pixel) será representado por um único pixel com a soma de todos os quatro;
#O valor máximo que um pixel deve ter, definido na terceira linha, deve ser o valor 
#original multiplicado por quatro devido a junção dos valores, conforme o item acima.

tipo = input().strip()

if tipo != "P2":
  exit()

dimensao = input().split()
COL, LIN = int(dimensao[0]), int(dimensao[1])

valor_maximo = int(input())

matriz = list()
for i in range(LIN):
  linha = input().split()

  valores = list()
  for item in linha:
    valores.append(int(item))
  matriz.append(valores)

nova_matriz = list()
for i in range(0, LIN, 2):
  nova_linha = list()
  for j in range(0, COL, 2):
    soma = matriz[i][j] + matriz[i+1][j] + matriz[i][j+1] + matriz[i+1][j+1]
    nova_linha.append(soma)
  nova_matriz.append(nova_linha)

nova_COL = COL//2
nova_LIN = LIN//2
novo_maximo = valor_maximo * 4

print("P2")
print(f"{nova_COL} {nova_LIN}")
print(novo_maximo)

for linha in nova_matriz:
  linhas_string= ""
  for item in linha:
    linhas_string += str(item) + " "
  linhas_string = linhas_string.rstrip()
  print(linhas_string)