soma_par = 0
cont_par = 0
soma_impar = 0
cont_impar = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma_par += num
        cont_par += 1
    else:
        soma_impar += num
        cont_impar += 1
print('Voce digitou {} numeros pares e a sua soma foi {}'.format(cont_par, soma_par))
print('Voce digitou {} numeros impares e a sua soma foi {}'.format(cont_impar, soma_impar))
