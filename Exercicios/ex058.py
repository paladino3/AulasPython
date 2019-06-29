"""
Melhore o jogo do DESAFIO 028 aonde o computador vai "pensar" em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários
para vencer.
"""

from random import randint
pcNum=randint(0,10)
tentativas=0
pare=1

print('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.')
print('Séra que você consegue adivinhar qual foi?')
while pare ==1:
    num=int(input('Qual é seu palpite? '))
    if num == pcNum:
        pare=0
        print('Acertou com {} tentativas. Parabéns!'.format(tentativas+1))
    elif (pcNum > num):
        tentativas+=1
        print('Mais... Tente mais uma vez.')
    elif (pcNum < num ) :
        tentativas+=1
        print('Menos... Tente mais uma vez.')


