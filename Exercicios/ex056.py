"""
Desenvolva um programa que leia o nome,idade,e sexo de 4 pessoas. no final do programa, mostre:

*A média de idade do grupo;
*Qual é o nome do homem mais velho;
*Quantas mulheres tem menos de 20 anos
"""
media=0
idadeMaior=0
qtdMenores=0
n=''
for c in range(1,5):
    nome=str(input('Digite o nome da {}ª pessoa:'.format(c)))
    idade=int(input('Digite a idade da {}ª pessoa:'.format(c)))
    sexo=str(input('Digite o sexo da {}ª pessoa: (M) ou (F)'.format(c))).upper()

    media+=idade

    if c ==1 and sexo == 'M':
        idadeMaior=idade
        n=nome
    else:
        if idade > idadeMaior and sexo == 'M':
            n=nome
            idadeMaior =  idade
        if sexo == 'F' and idade < 20:
            qtdMenores+=1

print('='*50)
print('A média de idades do grupo {:.1f} anos'.format(media/c))
print('O homem mais velho tem {} anos. Seu nome é: {}'.format(idadeMaior,n))
print('Quantidade de meninas com menos de 20 anos: {}'.format(qtdMenores))
print('='*50)
