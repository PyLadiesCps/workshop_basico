# Uma funcao que soma todos os elementos de uma lista


def soma(lista):
	'''Soma todos os elementos de uma lista'''
	soma = 0
	for num in lista:
		soma += num
	return soma


lista = map(int, input("Coloque uma sequencia de numeros: ").split(','))

print(soma(lista))
