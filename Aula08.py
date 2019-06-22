
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


from math import pow, sqrt

co=float(input('Digite o tamanho do Cateto Oposto: '))
ca=float(input('Digite o tamanho do Cateto Adjacente: '))

hip=sqrt(pow(co,2)+pow(ca,2))

print('O Cateto Oposto {}, Cateto Adjacente {} e o Tamanho da Hipotenusa {:.2f}'.format(co,ca,hip))