"""Crie um programa que leia o nome completo de uma pessoa e mostre:
*O nome com todas as letras maiuscolas

*O nome com todas as letras minusculas

*Quantas letras ao todo(sem considerar espaços)

*Quantas quatas letras tem o primeiro nome"""
"""Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender
são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(),
lower(), capitalize(), title(), strip(), junção com join()."""

nome=str(input('Digite seu nome completo: '))

print('\nSeu nome com todas letras maiúscula: {}'.format(nome.upper()))
print('Seu nome com todas letras minúscula: {}'.format(nome.lower()))
print('Seu nome possue {} caracteres sem espaços a mais'.format(len(nome.strip())))
dividido=nome.split()
print('Seu primeiro nome posssui {} caracteres'.format(len(dividido[0])))


