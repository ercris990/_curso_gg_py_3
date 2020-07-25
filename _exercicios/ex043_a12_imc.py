peso = float(input('Digite o seu peso - [Kg] '))
altura = float(input('Digite a sua altura em metros - [m] '))
imc = peso / (altura ** 2)
print('=+=' * 15)
print('O seu IMC é: {:.1f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso.')
elif 18.5 <= imc <= 25:
    print('Peso Ideal.')
elif 25 < imc <= 30:
    print('Sobrepeso.')
elif 30 < imc <= 40:
    print('Obesidade.')
else:
    print('Obesidade Mórbida.')
print('=+=' * 15)
