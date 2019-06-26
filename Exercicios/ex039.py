"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:

- Se ele ainda vai ser alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

*Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

hoje=2019
alistar=18

anoNascimento=int(input('Digite seu ano de nascimento: '))
if hoje-anoNascimento == alistar:
    print('Alistamento Obrigatório, você deve comparecer a junta de militar do exercito neste ano!')
elif hoje-anoNascimento > alistar:
    print('Você já passou  em {} anos, o ano do alistamento militar, vá urgente em uma junta militar do exercito'
          '.'.format((hoje-anoNascimento)-alistar))
else:
    print('Você ainda não completou 18 anos, para fazer parte da junta militar do exercito! Falta {} ano,s.'.format(alistar-(hoje-anoNascimento)))