"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
não atingiram a maioridade e quantas já são maiores (consiedere 21 anos);
"""
maior=0

for c in range(1,8):
    ano=int(input('Digite sua idade:'))
    if ano >= 21:
        c=maior+1
        print(c)