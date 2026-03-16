#while True:
 #letra = input()
  #print(f"Código: {ord(letra)}") 
  #retorna o numero Unicode de cada letra

#for i in range(0,3000):
  #print(chr(i), end=" ")
  #retorna os primeiros 3000 characteres da tabela Unicode
  #end=" " faz o print colocar um espaço apos cada saida em vez de pular linha

#fruta = "Banana"
#i = 0
#while i<len(fruta):
  #print(fruta[i], ord(fruta[i]))
  #i+=1
  #len() retorna o número de caracteres de uma string

#fruta[0] caracter 0 da string
#fruta[0:4]
#fruta[2:]
#fruta[inicio:fim:passo]
#fruta[len(fruta) - 1] retorna ultima letra
#fruta.title() primeira letra de cada palavra maiuscula
#fruta.upper() todas as letras maiusculas
#fruta.lower() todas as letras minusculas
#fruta.strip() tira espaços
#fruta.rstrip() tira espaço da direita
#fruta.lstrip() tira espaco da esquerda
#fruta.replace("nana", "ga") troca parte da string
#fruta.replace("a", "X") troc todos os "a" da string por "X"
#"12345".isdigt() verifica se todos os caracteres são numeros/digitos
#"fruta" + "verde" retorna "frutaverde"
#"B" * 5 retorna "BBBBB"

frase = " Hidrogenio liquido" 
print(frase.split()) #transforma em uma lista
print(frase.split(" "))

def gerar_emoticons():
  prefixo = ":-"

  for letra in ")(D*ox":
    print(prefixo+letra)

print(gerar_emoticons())