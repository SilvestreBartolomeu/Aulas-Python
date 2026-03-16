n = int(input())
Lista = list()

#cria lista numerica
for i in range(n):
  Lista.append(int(input()))

print(Lista)

print(len(Lista)) #tamanho
print(min(Lista)) #valor minimo
print(max(Lista)) #valor maximo
print(sum(Lista)) #soma dos valores

Lista2 = [99, 55, 66, 33, 99, 44, 11]

Lista2.sort() #ordena a lista em ordem crescente
print(Lista2)

Lista2.reverse() #reverte a lista
print(Lista2)

frase = input()
Lista3 = list()

#cria lista de palavras
for elemento in frase.split(" "):
  Lista3.append(elemento)

print(Lista3)