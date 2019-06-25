"""
Desenvolva um programa que pergunta a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 para viagens mais longas.
"""
km=200
viagem=int(input('Digite a distância a ser percorrida em Km: '))
if viagem >= km:
    print('Distância a ser percorrida {}Km, valor a ser pago R${}! Sendo cobrado R$0,50 centavos por Km!'.format(viagem,viagem*0.50))
else:
    print('Distância a ser percorrida {}Km, valor a ser pago R${}! Sendo cobrado R$0,45 centavos por Km!'.format(
        viagem,viagem * 0.45))