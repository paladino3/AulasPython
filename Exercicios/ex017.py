"""
Desafio 017
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo,
calcule e mostre o comprimento da hipotenusa.
"""
from math import pow, sqrt

co=float(input('Digite o tamanho do Cateto Oposto: '))
ca=float(input('Digite o tamanho do Cateto Adjacente: '))

hip=((co**2)+(ca**2))
hip=hip**2;
print('O Cateto Oposto {}, Cateto Adjacente {} e o Tamanho da Hipotenusa {:.0f}'.format(co,ca,hip**2))
