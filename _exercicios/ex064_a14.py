n = soma = cont = 0
n = int(input('Digite um numero [999 para parar]: '))
while n != 999:
    soma += n       # soma todos numeros digitados
    cont += 1       # acrescenta 1 a cada loop
    n = int(input('Digite um numero [999 para parar]: '))
print('=' * 43)
print('Voce digitou {} numeros e a sua soma foi {}.'.format(cont, soma))
