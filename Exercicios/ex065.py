"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
se ele quer ou não continuar a digitar valores.
"""
media=0
soma=0

res='N'
while res == 'N':
    n = int(input('Digite um número inteiro:'))

    res=str(input('Deseja continuar? [S/N]')).upper()
