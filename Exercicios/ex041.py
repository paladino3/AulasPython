idade=int(input('Digite sua idade: '))
"""
A confederação Nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
*Até 9 anos: MIRIM
*Até 14 anos: INFANTIL
*Até 19 anos: JUNIOR
*Até 20 anos: SENIOR
*Acima : MASTER

"""
if   idade >= 9 and idade <=13:
    print('Idade:{} anos,MIRIM '.format(idade))
elif(idade >=14 and idade <= 18):
    print('Idade:{} anos,INFANTIL '.format(idade))
elif(idade == 20 ):
    print('Idade:{} anos,SENIOR '.format(idade))
elif(idade > 20  ):
    print('Idade:{} anos,MASTER '.format(idade))
else:
    print('Idade:{} anos,Não pertence a uma categoria registrada pela confederação Nacional de natação!  '.format(idade))

