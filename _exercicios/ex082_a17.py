numList = []
par = []
impar = []
cont = 0
print('=--=' * 15)
while True:
    num = int(input('Digite um número: '))
    numList.append(num)
    cont += 1
    opc = str(input('Deseja continuar? [S/N] '))
    while opc not in 'SsNn':
        opc = str(input('Digite [S] para continuar e [N] para parar: '))
    if opc in 'Nn':
        break
for indice, valores in enumerate(numList):
    if valores % 2 == 0:
        par.append(valores)
    elif valores % 2 == 1:
        impar.append(valores)
print('=--=' * 15)
print(f'Lista completa: {numList}')
print(f'A lista contem {cont} valores.')
print(f'Lista dos pares: {par}')
print(f'Lista dos ímpares: {impar}')
print('=--=' * 15)
