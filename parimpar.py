jogador = input("Você escolhe par ou impar?")
if jogador == 'par':
	computador = 'impar'
else:
	computador = 'par'

print("O jogador é", jogador, "eu escolhi", computador)

numero_jogador = input("Escolha um numero: ")

print("O jogador escolheu", numero_jogador)

if computador == 'par':
	if int(numero_jogador) % 2 == 0:
		print("Numero do jogador é par")
		numero_computador = 2
	else:
		print("Numero do jogador é ímpar")
		numero_computador = 1
else: #computador é ímpar
	if int(numero_jogador) % 2 == 0:
		print("Numero do jogador é par")
		numero_computador = 1
	else:
		print("Numero do jogador é ímpar")
		numero_computador = 2

print("O computador escolheu", numero_computador, 
		"A soma é", int(numero_jogador)+numero_computador)
print("O computador ganhou!")