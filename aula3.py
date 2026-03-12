#Faça um laço principal que vai de um até o primeiro número fornecido (inclusive).
#Faça um laço secudário dentro do principal que vai do segundo núemero fornecido até 1 (inclusive), com contagem decrescente.
#Para cada combinação dos laços acima, some o primeiro número com o segundo número:
#Se for número primo, não faça nada (ignore a iteração atual).
#Senão, imprima o par de valores atuais da iteração.
#O terceiro valor recebido serve para limitar a quantidade de linha de saída, ou seja, a quantidade de pares impressos não pode exceder o terceiro valor.
#Caso todos os pares forem processados e não atingir o limite, imprimir como última linha a quantidade de linhas restantes.

def primo(n):
  if n<2:
    return False
  for i in range(2, int(n**0.5)+1):
    if n%i==0:
      return False
  return True

a = int(input())
b = int(input())
limite = int(input())

n_pares = 0

for i in range(1, a+1):
  for j in range(b, 0, -1):
    soma = i+j
    if primo(soma):
      continue
    if n_pares<limite:
      print(i, j)
      n_pares+=1
    else:
      break
  if n_pares >= limite:
    break

if limite > n_pares:
  print(limite-n_pares)