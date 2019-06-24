"""
Faça um programa que leia o nome completo de uma pessoa.
mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria Souza
Primeiro= Ana
Último= Souza
"""

n=str(input('Digite seu nome completo: ')).strip()

nome=n.split()

print('Nome completo= {}.'.format(n))
print('Primeiro nome= {}.'.format(nome[0]))
print('Último nome= {}.'.format(nome[len(nome)-1]))

#print(nome)=['wesley', 'rolim', 'simoes'] 0 1 2(simoes)
#print(len(nome))= 3(3-1=2)
