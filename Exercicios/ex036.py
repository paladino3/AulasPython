"""
Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
*O programa vai perguntar o  VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.

*Calcule o valor da prestação mensal. Sabendo que ela não pode exceder 30% do salário ou
então o emprestimo será negado.
"""

print('{}Financiamento da casa própria{}'.format('-'*10,'-'*10))
valor=int(input('Digite o valor do imovél R$: '))
anos=int(input('Digite o número de anos que deseja financial o imovél: '))
salario=int(input('Digite sua renda mensal R$:'))
meses=anos*12
valorPrestacacao=(valor/meses)
aprovacao=(salario*0.30)
print('Sua parcela será em {} meses'.format(meses))
print('Valor da prestação R${} mensal'.format(valorPrestacacao))
print('30% do seu salário R${}'.format(aprovacao))
if  valorPrestacacao >= aprovacao:
    print('Infelizmente o financiamento NÃO foi Aprovado!')
else:
    print('Parabéns. Financiamento FOI Aprovado!')
