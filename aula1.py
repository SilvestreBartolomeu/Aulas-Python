x = 1 #int
y = "banana" #string
z = 2.6 #float
m = False #bool #strings vazias sempre retornam falso e as com conetudo retornam verdadeiro
n1=5;n2=2; p=complex(n1,n2); q=complex(4j) #numero complexo

a=["carro", "aviao", "navio", 1, 5.8, True] #list/array #é possivel colocar tipos diferentes nela
#digitando a[0]="moto" muda o valor dentro da lista. Isso nao acontece com a tupla
b=("carro", "aviao", "navio", 1, 5.8, True) #tupla

c=range(0, 100, 1) #List #cria lista de 0 a 100 indo de 1 em 1
d={ #dict
    "nome" : "silvestre",
    "idade" : "dezenove" #chave : valor

}

e={5,7,4,5,7,4,8} #set #nao repete valores
f=frozenset({5,7,4,5,7,4,8}) #set #impede que o set mude

"""print("Valor da variavel: "+str(x))
print("Tipo: "+str(type(x)))"""
#str() transforma em string (so pode somar variaveis do mesmo tipo com o +)

print("Valor da variavel: ", x)
print("Tipo: ", type(x))
print("Tipo: ", type(y))
print("Tipo: ", type(z))
print("Tipo: ", type(m))
print(p.real, p.imag)
print(q.real, q.imag)
print("Tipo: ", type(p))
print("Valor:", a[0]) #a[0] imprime o primeiro valor da lista
print("Tipo: ", type(a))
print("Valor: ", d["nome"])
print("Valor: ", e)
print("Valor: ", f)