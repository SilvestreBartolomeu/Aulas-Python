def conta_divisores(numero: int) -> int:
  divisor = 0
  for i in range(1, numero + 1):
    if numero%i == 0:
      divisor+=1
  return divisor

def soma_divisores(numero: int) -> int:
  soma = 0
  for i in range(1, numero):
    if numero%i == 0:
      soma += i
  return soma

def verifica_numeros_amigos(a: int, b: int) -> bool:
  if a == soma_divisores(b) and b == soma_divisores(a):
    return True
  return False

def conta_par_numeros_amigos(de: int, ate: int) -> int:
  pares = 0
  for i in range(de, ate + 1):
    for j in range(i + 1, ate + 1):
      if verifica_numeros_amigos(i, j):
        pares += 1
  return pares

def primo(numero):
  if numero < 2:
    return False
  for i in range(2, int(numero**0.5) + 1):
    if numero%i == 0:
      return False
  return True

def conta_decomposicao_primos(numero: int) -> int:
  quantidade_primo = 0
  for i in range(2, numero):
    if primo(i):
      if numero%i == 0:
        quantidade_primo += 1
        while numero%i == 0:
          numero //= i

  return quantidade_primo