#Faça um programa que verifica a Similaridade J entre duas ou mais pessoas
#retorna as respectivas similaridades entre elas
#O primeiro argumento é um valor inteiro que representa a quantidade de pessoas.
#cada linha representa uma pessoa e suas respectivas preferências
#primeira palavra da linha é o nome, e as demais são os itens de preferência
#A lista com a combinações de todas as pessoas e sua respectiva Similaridade J, em ordem decrescente de similaridade
#codigo com ordenacao sem usar sort ou sorted

def ordenar(Lista):
  tamanho = len(Lista)

  for k in range(len(Lista)):
    for j in range(len(Lista) -1 -k):
      if Lista[j][2] < Lista[j+1][2]:
        Lista[j], Lista[j+1] = Lista[j+1], Lista[j]

numero_de_pessoas = int(input())

nomes = list()
preferencias = list()
for pessoas in range(numero_de_pessoas):
  linha = input().split()
  nomes.append(linha[0])
  preferencias.append(linha[1:])

lista_final = list()
for i in range(numero_de_pessoas):
  for j in range(i + 1, numero_de_pessoas):

    intersecao = 0
    lista = list()
    for item in preferencias[i]:
      if item in preferencias[j]:
        intersecao += 1
        
    for item in (preferencias[i] + preferencias[j]):
      if item not in lista:
        lista.append(item)
        
    uniao = len(lista)

    if uniao == 0:
      similaridade = 0

    else:
      similaridade = intersecao/uniao

    lista_final.append((nomes[i], nomes[j], similaridade))

ordenar(lista_final)
for i in range(len(lista_final)):
  print(f"{lista_final[i][0]} e {lista_final[i][1]} ({lista_final[i][2]})")