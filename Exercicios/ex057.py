"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F', caso esteja errado, peça a digitação
novamente até um valor correto.
"""
pare= True
while pare != False:
    sex=str(input('Digite seu sexo [M/F]:')).upper()
    if sex == 'M' or sex == 'F':
        pare=False
print('fim')