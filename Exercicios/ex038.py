"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
*O primeiro valor é maior
*O segunda valor é maior
*Não existe valor maior, os dois são iguais
"""
A=int(input('Digite um numero 1: '))
B=int(input('Digite um numero 2: '))

if A > B :
    print('O número(1): {} é maior que o número(2): {}'.format(A,B))
elif B > A:
    print('O número(2): {} é maior que o número(1): {}'.format(B, A))
else:
    print('Os dois números são iguais {} = {}'.format(A,B))