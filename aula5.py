frutas = ["banana", "laranja", "limão", "abacaxi"]
frutas2 = list(frutas)

print(frutas[0], frutas[-1])

frutas[1] = "melancia"
#adiciona um objeto no lugar de outro objeto dentro da lista
print(frutas[1])

frutas.append("pera")
#adiciona um novo objeto
print(frutas)

frutas.remove("pera")
#remove um objeto
print(frutas)

del frutas[3]
#remove um objeto de uma certa posição
print(frutas)

frutas.pop()
#remove ultimo elemento da lista
print(frutas)

#da mesma forma que o len retorna o numero de caracteres de uma string,
#ele retorna o numero de objetos na lista
print(f"{len(frutas)} frutas")

frutas.clear()
#limpa a lista
print(frutas)

print(frutas2)

frutas3 = frutas2 + frutas2
#soma listas
print(frutas3)