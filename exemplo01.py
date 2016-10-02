# Comentario curto
''' Comentario longo ... 
ou pelo menos deveria ser'''

def soma(a, b):
	''' Esta funcao soma dois termos'''
	return a + b


def multiplica(a, b):
	''' Esta funcao multiplica dois termos'''
	return a*b


def potencia(a, b):
	''' Esta funcao faz a elevado a b'''
	return a**b


a = int(input("Digite um numero: "))
b = int(input("Digite um numero: "))
c = int(input("Digite um numero:"))

print(multiplica(a, b))
print(soma(a, b))
print(potencia(a, b))
print(multiplica(soma(a, b), c))