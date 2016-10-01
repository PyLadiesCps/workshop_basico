#! /bin/python3
# coding: utf-8
import random
quero = random.randint(0,3)
if quero ==1: 
	print('Eu escolho ímpar')
elif quero <= 1:
	print('Eu escolho par')
else: # > 1, usuario decide
	quero = 1 - int (input('Par(0) ou ímpar(1)?'))
computador = random.randint(0,10)
jogador = int(input('Quantos dedos vc colocou?'))
total = computador + jogador
print('Eu coloquei '+str(computador)+ ' entao deu '+ str(total))
if quero == total % 2:
	print('Eu ganhei!')
else:
	print('Você ganhou')