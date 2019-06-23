
""""
from math import sqrt

num=int(input('Digite um número: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {:.3f}'.format(num, raiz))
"""

#Desafio 016
# Crie um programa que leia um numero Real qualquer, pelo teclado e mostre na tela a sua porçao inteira
#Exemplo 6.127 fica = 6
"""
numero=float(input('Digite um numero real: '))
print('Seu numero real: {}, e sua porção inteira: {:.0f}'.format(numero,numero))
"""
#Desafio 017
#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo,
# calcule e mostre o comprimento da hipotenusa

"""
from math import pow, sqrt

co=float(input('Digite o tamanho do Cateto Oposto: '))
ca=float(input('Digite o tamanho do Cateto Adjacente: '))

hip=((co**2)+(ca**2))

print('O Cateto Oposto {}, Cateto Adjacente {} e o Tamanho da Hipotenusa {:.1f}'.format(co,ca,hip**2))
"""

#Desafio 018
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#cosseno a tangente desse ângulo.


#Desafio 019
#Um professor quer sortear um dos seus quatro alunos para apagar o quadro, faça um programa
#que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

import random


a1=str(input('Digite o nome do Primeiro Aluno: '))
a2=str(input('Digite o nome do Segundo Aluno: '))
a3=str(input('Digite o nome do Terceiro Aluno: '))
a4=str(input('Digite o nome do Quarto Aluno: '))

lista=[a1,a2,a3,a4]
escolha=random.choice(lista)

print('O aluno escolhido foi: {} '.format(escolha))





