"""
Crie um programa que leia uma frase qualquer e diga se ela é um PALÍNDROMO, desconsiderando os espaços.
EX: APOS A SOPA
EX: A SACADA DA CASA
EX: A TORRE DA DERROTA
EX: O LOBO AMA O BOLO
EX: ANOTARAM A DATA DA MARATONA
"""

frase=str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
juntar=''.join(palavras)
"""
inverso=''
for letra in range(len(juntar)-1,-1,-1):
    inverso += juntar[letra]
"""
inverso=juntar[::-1]

if inverso == juntar:
    print('A frase digitada:{} o inverso da frase:{}'.format(juntar,inverso))
    print('Temos um palíndromo!')
else:
    print('A frase digitada:{} o inverso da frase:{}'.format(juntar, inverso))
    print('A frase digitada não é um palíndromo!')