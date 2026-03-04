def inverte_caracteres(frase):
  inversao = ""
  
  for i in range(len(frase) - 1, -1, -1):
    inversao += frase[i]

  return inversao

def inverte_caracteres_em_palavras(frase):
  inversao = ""
  palavra = ""

  for i in range(len(frase)):
    if frase[i] != " ":
      palavra += frase[i]
    else:
      inversao += palavra[::-1] + " "
      palavra = ""
  inversao += palavra[::-1]

  return inversao

def inverte_palavras(frase):
  frase_invertida = inverte_caracteres(frase)
  inversao = ""
  palavra = ""

  for i in range(len(frase_invertida)):
    if frase_invertida[i] != " ":
      palavra += frase_invertida[i]
    else:
      inversao += palavra[::-1] + " "
      palavra = ""
  inversao += palavra[::-1]

  return inversao