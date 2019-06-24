"""
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome"SANTO".
"""

cidade=str(input('Digite um nome de cidade: ')).strip()


res=cidade.upper().find('SANTO')
if res == 0:
    print('Sua cidade começa com a palavra "SANTO". {}'.format(cidade.upper()))
else:
    print('Sua cidade não começa com a palavra "SANTO" na frase: {}'.format(cidade))

