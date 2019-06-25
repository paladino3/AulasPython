"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.

Para salários superiores a R$1.250,00, calcule um aumento de 10%.

Para inferiores ou iguais, o aumento é de 15%.
"""

salario=(int(input('Digite seu salário: ')))

if salario <= 1250:
    total=salario*0.15
    print('Salário antigo R${}, novo valor reajustado R${}'.format(salario,salario+total))
else:
    total = salario * 0.10
    print('Salário antigo R${}, novo valor reajustado R${}'.format(salario,salario+ total))