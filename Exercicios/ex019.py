"""
Desafio 019
Um professor quer sortear um dos seus quatro alunos para apagar o quadro, faça um programa
que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
"""
import random

a1=str(input('Digite o nome do Primeiro Aluno: '))
a2=str(input('Digite o nome do Segundo Aluno: '))
a3=str(input('Digite o nome do Terceiro Aluno: '))
a4=str(input('Digite o nome do Quarto Aluno: '))

lista=[a1,a2,a3,a4]
escolha=random.choice(lista)

print('O aluno escolhido foi: {} '.format(escolha))


