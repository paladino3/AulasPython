"""
Crie um programa que faça o computador jogar JOKENPÔ com você
"""
print('{}''JOKENPÔ''{}'.format('='*15,'='*15))
seletc=int(input('\nEscolha:\n1- Papel\n2- Pedra\n3- Tesoura\nSua resposta de 0 a 3:'))

lista=['Papel','Pedra','Tesoura']

from random import randint

aleatorio=randint(0,2)

if seletc == 1 & aleatorio == 1:
    print('Sua escolha {}, escolha do computador {}. Você venceu'.format(lista[0],lista[1]))
elif(seletc == 2 & aleatorio == 1):
    print('Sua escolha {}, escolha do computador {}. Você perdeu'.format(lista[1],lista[0]))
