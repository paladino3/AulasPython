"""
#Escreva um programa que leia a velocidade de um carro.
#Se a velocidade ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7,00 por cada  Km acima do limite.
"""
limite=80

speed=int(input('Digite a velocidade instantânea em Km/h: '))
if speed <= 80 :
    print('Velocidade dentro do limite estabelecido!')
else:


    multa=(speed-limite)*7
    print('Você ultrapassou o limite estabelecido em {}Km/h, e deverá'
          ' pagar uma multa no valor de R${:.2f}!'.format(speed-limite,multa))