matriz = [[], [], []]
linha1 = linha2 = linha3 = 0
for c in range(0, 3):
    linha1 = int(input(f'Digite um valor para [0, {c}]: '))
    matriz[0].append(linha1)
for c in range(0, 3):
    linha2 = int(input(f'Digite um valor para [1, {c}]: '))
    matriz[1].append(linha2)
for c in range(0, 3):
    linha3 = int(input(f'Digite um valor para [2, {c}]: '))
    matriz[2].append(linha3)
print('{:=^50}'.format(' MATRIZ '))
print(f'[{matriz[0][0]}][{matriz[0][1]}][{matriz[0][2]}]')
print(f'[{matriz[1][0]}][{matriz[1][1]}][{matriz[1][2]}]')
print(f'[{matriz[2][0]}][{matriz[2][1]}][{matriz[2][2]}]')
