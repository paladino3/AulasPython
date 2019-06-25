"""
Faça um programa que leia três números e mostre qual é o MAIOR e qual  é o Menor.
"""
print('Digite três números: ')
A=int(input('Número 1: '))
B=int(input('Número 2: '))
C=int(input('Número 3: '))

if (A >= B & B >= C):
    print('Número:{} é maior do que {}, e também maior do que {}.'.format(A,B,C))
elif(B >= A & A >= C):
    print('Número:{} é maior do que {}, e támbem maior do que {}'.format(B,A,C))
elif(C >= A & A >= B):
    print('Número:{} é maior do que {}, e támbem maior do que {}'.format(C,A,B))
elif(C >= B & B >= A):
    print('Número:{} é maior do que {}, e támbem maior do que {}'.format(C,B,A))
elif(B >= C & C >= A):
    print('Número:{} é maior do que {}, e támbem maior do que {}'.format(B,C,A))
else:
    print('Número:{} é maior do que {}, e támbem maior do que {}'.format(A,C,B))

