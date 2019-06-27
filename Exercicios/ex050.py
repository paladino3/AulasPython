"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""
soma=0
cont=0
for c in range(1,7):
    cont+=1
    n=int(input('({})Digite um número inteiro:'.format(cont)))
    if n % 2== 0:
        soma+=n

print('A soma dos valores pares:{} '.format(soma))