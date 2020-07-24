from time import sleep
l1 = list()
l2 = list()
l3 = list()
matriz = [l1, l2, l3]
s = list()
c = 1
for cont in range(0, 3):
    print(f'============ {c}ª COLUNA ============')
    l1.append(int(input(f'Digite um valor para [{cont}, 0]: ')))
    l2.append(int(input(f'Digite um valor para [{cont}, 1]: ')))
    l3.append(int(input(f'Digite um valor para [{cont}, 2]: ')))
    c += 1
soma = l1[2] + l2[2] + l3[2]
s.append(soma)
print('*' * 36)
print('CARREGANDO', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.', end='')
sleep(0.5)
print('.')
sleep(0.5)
print('{:*^36}'.format(' MATRIZ '))
print(f'{l1}')
print(f'{l2}')
print(f'{l3}')
print('*' * 36)

#print(f'A soma entre {l1[2]} e {l2[2]} {l3[2]} é {s}')
#print('*' * 36)
# print(matriz)
