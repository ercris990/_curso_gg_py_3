soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1           # cont = cont + 1
        soma += c           # soma = soma + c
print('Quntidade de numeros impares multiplos de 3 entre 0 e 500: {}'.format(cont))
print('Soma de todos os numeros impares multiplos de 3 entre 0 e 500: {}'.format(soma))
