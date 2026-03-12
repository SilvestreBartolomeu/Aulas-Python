def inverte_caracteres(frase):
  inversao = ""
  for i in range(len(frase) - 1, -1, -1):
    inversao += frase[i]
  return inversao
# Retorna a palavra/frase invertida.
# Dica: Faça um laço decrescente copiando o texto original para uma string.
# Exemplo 1:
# Entrada: ABCDEF
# Saída: FEDCBA
# Exemplo 2:
# Entrada: Universidade Federal do ABC
# Saída: CBA od laredeF edadisrevinU

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
# Retorna a frase apenas com as palavras invertidas.
# A ordem das palavras são preservadas.
# Dica: faça um laço até o fim da palavra (identifcado por espaço ou final).
# Utilize esta inforamção para extrair e inverter a palavra.
# Exemplo 1:
# Entrada: ABC DEF GHI
# Saída: CBA FED IHG
# Exemplo 2:
# Entrada: Arara voa leve
# Saída: ararA aov evel

def inverte_palavras(frase):
  inversao = inverte_caracteres_em_palavras(inverte_caracteres(frase))
  return inversao
# Retorna as palavras invertidas, mas não os caracteres.
# Dica: faça um laço decrescente até o início da plavra.
# Utilize esta informação para copiar a palavra para um novo texto.
# Exemplo 1:
# Entrada: ABC DEF GHI
# Saída: GHI DEF ABC
# Exemplo 2:
# Entrada: Hoje não chove
# Saída: chove não Hoje