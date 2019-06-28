"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores (consiedere 21 anos);
"""

from datetime import date
maior=0
menor=0
idade=0

for c in range(1,8):

    ano = int(input('Digite ano do nascimento da {}ª pessoa:'.format(c)))
    idade=(date.today().year-ano)
    if idade >=21:
        maior+=1
    else:
        menor+=1
print('MAIORES de 21 anos: {} pessoas, e MENORES de 21 anos: {} pessoas;'.format(maior,menor))