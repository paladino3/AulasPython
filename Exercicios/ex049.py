"""
Refaça DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
"""
n=int(input('Digite um número para ver sua tabuada: '))
for c in range (1,11):
    res=c*n
    print('{} x {} = {}'.format(n,c,res))
