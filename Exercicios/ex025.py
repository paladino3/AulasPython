"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome=str(input('Digite seu nome completo: '))
nome.lower()
res= 'silva' in nome

if res == True:
    print('\n Nome digitado: {}, Seu nome contém a palavra "SILVA".'.format(nome))
else:
    print('\n Nome digitado: {}, Seu nome NÃO contém a palavra "SILVA".'.format(nome))