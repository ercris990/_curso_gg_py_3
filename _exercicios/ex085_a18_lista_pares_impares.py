numlist = [[], []]
valores = 0
print('=:=' * 20)
for i in range(1, 8):
    valores = int(input(f'Digite o {i}º numero: '))
    if valores % 2 == 0:
        numlist[0].append(valores)
    else:
        numlist[1].append(valores)
print('=:=' * 20)
print(f'Lista de pares: {sorted(numlist[0])}')
print(f'Lista de ímpares: {sorted(numlist[1])}')
