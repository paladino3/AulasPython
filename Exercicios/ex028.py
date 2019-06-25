"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint

print('Computador "pensa", em um número entre 0 e 5...')
user=int(input('Digite um número que o computador irá pensar:  '))

comp=randint(0,5)
if user == comp:
    print('O número escolhido é: {}'.format(comp))
    print('Parabéns! você venceu.')
else:
    print('O número escolhido pelo computador é: {}'.format(comp))
    print('Você perdeu...')

