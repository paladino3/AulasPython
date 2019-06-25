"""
Faça um programa que leia três números e mostre qual é o MAIOR e qual  é o Menor.
"""
print('Digite três números: ')
A=int(input('Número 1: '))
B=int(input('Número 2: '))
C=int(input('Número 3: '))

if (A > B & A > C & C > B):
    print('Número:{} é maior do que {}, e também maior que {}.'.format(A,C,B))
elif(B > A & B > C & C > A):
    print('Número:{} é maior do que {}, e támbem maior que {}'.format(B, C, A))
else:
    print('Número:{} é maior do que {}, e támbem maior que {}'.format(C,A,B))