"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu PREÇO NORMAL e
CONDIÇÃO DE PAGAMENTO:

* À vista dinheiro/cheque: 10% de desconto
* À vista no cartão: 5% de desconto
* Em até 2x no cartão: preço normal

* 3x ou mais no cartão: 20% de juros
"""
selecao=0
produto=float(input('Digite o valor do produto R$:'))
formaPag=('Digite a forma de pagamento:\n1- Dinheiro.\n2- Cheque.\n3- Cartão.')
if formaPag == 1:
    print('O valor do produto R${} com 10% de desconto ;)'.format(produto-(produto*0.10)))
elif( formaPag == 2 ):
    print('O valor do produto R${} com 10% de desconto ;)'.format(produto - (produto * 0.10)))
elif( formaPag == 3 and selecao == 1 and selecao == 2):
    selecao=int(input('Em quantas vez deseja fazer? Até 2x sem Juros'))
    print('O valor do produto R${} em {} vezes em juros ;)'.format(produto,selecao))
else:
    print('O valor do produto R${} e o número:{} de vezes, com 20% de juros ;)'.format(produto + (produto * 0.20)))