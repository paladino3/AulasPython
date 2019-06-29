"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1]somar
[2]multiplicar
[3]maior
[4]novos números
[5]sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
maior=0
multiplicar=0
soma=0
res=0

print('—' * 50)
n1=int(input('Digite um número:'))
n2=int(input('Digite um novo número:'))
print('Valores digitados ({}) e ({})'.format(n1, n2))
while res!=1:
    func=int(input('[1]Somar\n[2]Multiplicar\n[3]Maior\n[4]Novos números\n[5]Sair do programa\nEscolha: '))
    print('—'*50)
    if func == 1:
        soma=n1+n2
        print('A soma dos dois números é: {}'.format(soma))
        print('—' * 50)
    elif( func == 2 ):
        multiplicar=n1*n2
        print('A multiplicação dos dois números é: {}'.format(multiplicar))
        print('—' * 50)
    elif( func == 3):
        if n1 > n2:
            print('O número maior digitado é: {}, e o menor número é:{}'.format(n1,n2))
            print('—' * 50)
        elif n2 > n1:
            print('O número maior digitado é: {}, e o menor número é:{}'.format(n2, n1))
            print('—' * 50)
        else:
            print('Os dois números são iguais {} = {}'.format(n1,n2))
            print('—' * 50)
    elif( func == 4 ):
        n1 = int(input('Digite um número:'))
        n2 = int(input('Digite um novo número:'))
        n1=n1
        n2=n2
    elif( func ==5 ):
        res=1
        print('Fim')