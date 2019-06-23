"""
Faça um programa que leia uma frase pelo teclado e mostre:

*Quantas vezes aparece a letra "A".

*Em que posição ela aparece a primeira vez.

*Em que posição ela aparece a ultima vez.

"""

frase=str(input('Digite uma frase qualquer: '))
frase=frase.upper()
print(frase.count(('A')))
print(frase[::])
print(frase.find('A'))



