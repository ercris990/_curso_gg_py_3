n = soma = cont = media = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    soma += n
    cont += 1
media = soma/cont
print('»«' * 25)
print(f'Voce digitou {cont} números.')
print(f'A soma de todos os números digitados vale: {soma}.')
print(f'A media dos valores digitados é: {media:.1f}')
print('«»' * 25)
