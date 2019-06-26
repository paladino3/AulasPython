"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela abaixo:

*Abaixo de 18.5: Abaixo do peso
*Entre 18.5 e 25: Peso ideal
*25 até 30: Sobrepeso
*30 até 40: Obesidade
*Acima de 40: Obesidade mórbida

#Formula= peso / 2x altura

"""

altura=float(input('Digite sua altura: '))
peso=float(input('Digite seu peso: '))

imc=(peso)/(altura*altura)

print('Sua Altura:{} e seu Peso:{}, seu IMC={:.2f}'.format(altura,peso,imc))
if imc < 18.5:
    print('Abaixo do peso!')
elif( imc > 18.5 and imc <= 25):
    print('Peso ideal!')
elif(imc > 25 and imc <= 30 ):
    print('Sobrepeso!')
elif(imc > 30 and imc <=40 ):
    print('Obesidade!')
elif(imc > 40 ):
    print('Obesidade mórbida')
else:
    print('Valores incorretos!!!')