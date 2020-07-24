num = cont = soma = 0
while True:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    cont += 1
    soma += num
print('++' * 19)
print(f'Voçê digitou: {cont} valores.\nA soma dos valores digitados é: {soma}')
