"""
Crie um programa que faça o computador jogar JOKENPÔ com você
"""
resp = 's'
while resp == 's':

    from random import randint
    print('{}''JOKENPÔ''{}'.format('='*15,'='*15))
    seletc=int(input('\nEscolha:\n1- Papel\n2- Pedra\n3- Tesoura\nSua resposta de 0 a 3: '))

    lista=['Papel','Pedra','Tesoura']
    aleatorio=randint(1,3)

    if  seletc == 1 and aleatorio == 1:
        print('Sua escolha {}, escolha do computador ({}={}). Empate!'.format(lista[0],aleatorio,lista[0]))
    elif(seletc == 1 and aleatorio == 2):
        print('Sua escolha {}, escolha do computador ({}={}). Você venceu!'.format(lista[0],2,lista[1]))
    elif(seletc == 1 and aleatorio == 3):
        print('Sua escolha {}, escolha do computador ({}={}). Você perdeu!'.format(lista[0],3,lista[2]))
    elif(seletc == 2 and aleatorio == 2):
        print('Sua escolha {}, escolha do computador ({}={}). Empate!'.format(lista[1],2,lista[1]))
    elif(seletc == 2 and aleatorio == 3):
        print('Sua escolha {}, escolha do computador ({}={}). Você venceu!'.format(lista[1],3,lista[2]))
    elif(seletc == 2 and aleatorio == 1):
        print('Sua escolha {}, escolha do computador ({}={}). Você perdeu!'.format(lista[1],1,lista[0]))
    elif(seletc == 3 and aleatorio == 3):
        print('Sua escolha {}, escolha do computador ({}={}). Empate!'.format(lista[2],3,lista[2]))
    elif(seletc == 3 and aleatorio == 1):
        print('Sua escolha {}, escolha do computador ({}={}). Você venceu!'.format(lista[2],1,lista[0]))
    elif(seletc == 3 and aleatorio == 2):
        print('Sua escolha {}, escolha do computador {},{}. Você perdeu!'.format(lista[2],2,lista[1]))
    else:
        print('Número inválido!')
    resp=str(input('Deseja continuar? (s) ou (n)'))

