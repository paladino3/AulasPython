"""
Crie um programa que leia duas notas de um aluno e calcule sua média. Mostrando uma mensagem com a média
atingida:

*Média abaixo de 5.0:
REPROVADO

*Média entre 5.0 e 6.9:
RECUPERAÇÃO

*Média 7.0 ou superior:
APROVADO
"""
n1=float(input('Digite sua primeira nota:'))
n2=float(input('Digite sua segunda nota:'))
media=(n1+n2)/2
print('Média: ',media)
if media >= 70.0:
    print('APROVADO! nota {}'.format(media))
elif media >= 50.0 and media <= 69.0:
    print('RECUPERAÇÃO! nota {}'.format(media))
else:
    print('REPROVADO! nota {}'.format(media))
