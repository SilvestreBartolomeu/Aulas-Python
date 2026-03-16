def inverter_lista(Lista):
    Lista_invertida = list()
    for i in range(len(Lista) -1, -1, -1):
      x = Lista[i]
      Lista_invertida.append(x)
    return Lista_invertida

    # Retorna a Lista com ordem invertida.
    # Usar laços para gerar a nova lista invertida.
    # Exemplo:
    # Entrada: [1, 2, 3, 4]
    # Saída: [4, 3, 2, 1]

def eliminar_elemento(x, Lista):
    nova_lista = list()
    for i in Lista:
      if i == x:
        continue
      else:
        nova_lista.append(i)
    return nova_lista

    # Retorna uma lista removendo todos os elementos de valor x (se houver).
    # Usar laços para remover.
    # Exemplos:
    # Entrada: x = 2 e Lista = [1, 2, 3, 4]
    # Saída: [1, 3, 4]
    # Entrada: x = 5 e Lista = [1, 2, 3, 4]
    # Saída: [1, 2, 3, 4]


def menor_elemento(Lista):
  valor = Lista[0]
  for i in Lista:
    if i < valor:
      valor = i
  return valor
    # Retorna o menor valor de uma lista.
    # Considere que a lista não tem valores repetidos.
    # Usar laços para buscar o menor valor.
    # Exemplo:
    # Entrada: [6, 4, 2, 5, 3]
    # Saída: 2

def segundo_menor_elemento(Lista):
  nova_lista = eliminar_elemento(menor_elemento(Lista), Lista)
  valor = menor_elemento(nova_lista)
  return valor

    # Retorna o segundo menor valor de uma lista.
    # Considere que a lista não tem valores repetidos.
    # Dica: você pode utilizar as duas funções acima!
    # Exemplos:
    # Entrada: [6, 2, 4, 3, 5]
    # Saída: 3


def agrupar_elementos(quantidade, Lista):
    nova_lista = list()
    for i in range(0, len(Lista), quantidade):
      soma = 0
      for j in range(0, quantidade):
        if i+j < len(Lista):
          soma += Lista[i+j]
      nova_lista.append(soma)
    return nova_lista

    # Retorna uma lista que agrupa em uma quantidade definida somando os valores.
    # Exemplos:
    # Entrada: quantidade = 2 e Lista = [1, 2, 3, 4, 5, 6]
    # Saída: [3, 7, 11]
    # Explicação: [1+2=3, 3+4=7, 5+6=11]
    # Entrada: quantidade = 3 e Lista = [1, 2, 3, 4, 5, 6]
    # Saída: [6, 15]
    # Explicação: [1+2+3=6, 4+5+6=15]
    # Entrada: quantidade = 2 e Lista = [1, 2, 3, 4, 5]
    # Saída: [3, 7, 5]
    # Explicação: [1+2=3, 3+4=7, 5=5]
    # Entrada: quantidade = 3 e Lista = [1, 2, 3, 4, 5]
    # Saída: [6, 9]
    # Explicação: [1+2+3=6, 4+5=9]