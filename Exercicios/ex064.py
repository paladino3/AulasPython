"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
digitar o valor 999. que é a condição de parada. No final, mostre quantos números foram
digitados e qual foi a soma entre eles (*Desconsiderando o flag).

"""
pare=1
soma=0
while  pare== 1:
    n = int(input('Digite um número: '))
    if n == 999:
        pare=0
        print('A soma de todos os números foi: ',soma)
    else:
        soma+=n
