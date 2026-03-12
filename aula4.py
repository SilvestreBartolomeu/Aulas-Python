def conta_divisores(numero: int) -> int:
  numero_divisores=0
  for i in range(1, numero + 1):
    if numero%i == 0:
      numero_divisores+=1
  return numero_divisores
# Retornar a quantidade de divisores de um número inteiro.
# Exemplo: 24
# Divisores: 1, 2, 3, 4, 6, 8, 12 e 24.
# Resposta: 8

def soma_divisores(numero: int) -> int:
  soma=0
  for i in range(1, numero):
    if numero%i == 0:
      soma+=i
  return soma
# Retorna a soma de todos os divisores de um número inteiro, excluíndo ele mesmo.
# Exemplo: 24
# Retorno: 1 + 2 + 3 + 4 + 6 + 8 + 12 = 36

def verifica_numeros_amigos(a: int, b: int) -> bool:
  if a == soma_divisores(b) and b == soma_divisores(a):
    return True
  return False
# Números amigos são dois números que estão ligados um ao outro por uma propriedade especial: cada um deles é a soma dos divisores do outro.
# Exemplo: Os divisores de 220 são 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 e 110., cuja soma é 284;
#          Os divisores de 284 são 1, 2, 4, 71 e 142, cuja soma é 220.
#          Os números 220 e 284 são amigos.
# Dica: Utilize a função acima!

def conta_par_numeros_amigos(de: int, ate: int) -> int:
  p = 0
  for i in range(de, ate + 1):
    for j in range(i + 1, ate + 1):
      if verifica_numeros_amigos(i, j):
        p+=1
  return p
# Conta a quantidade de pares de números amigos dentro de um intervalo entre 'de' e 'ate'.
# Exemplo 1: de = 50  e ate = 100, não há números amigos, ou seja, o retorno é 0.
# Exemplo 2: de = 200 e ate = 300, existe um par de números amigos (220, 284), ou seja, o retorno é 1.

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

# Decompor um número em fatores primos ou, fatorá-lo, é escrever este número como uma multiplicação de números primos.
# Os fatores são termos da multiplicação que, neste caso, são números primos.
# Esta função retorna a quantidade de fatores primos, excluíndo o 1 e o próprio número.
# Exemplo 1: 24 = 2 * 2 * 2 * 3, ou seja, tem dois fatores primos (2 e 3). O retorno é 2.
# Exemplo 2: 227 é um número primo, não tem fatores. O retorno é 0.
# Exemplo 3: 49 = 7 * 7, ou seja, tem apenas um fator primo (7). O retorno é 1.