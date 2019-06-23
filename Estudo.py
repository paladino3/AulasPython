
import random

tam=int(input('Digite o tamanho da Lista: '))
n=0
while tam > n:
    n=n+1
    nome=str(input('Digite o nome do aluno {}: '.format(n)))

lista=[nome]
for i in lista:
    print(i)
