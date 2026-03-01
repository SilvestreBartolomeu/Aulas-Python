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