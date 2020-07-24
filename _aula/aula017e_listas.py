a = [2, 3, 4, 7]
b = a       # lista B é igual a lista A
b[2] = 8    # substitui o elemento da posição 2 pelo 8 nas duas listas
c = a[:]    # lista C recebe uma copia dos elementos da lista A
c[1] = 8    # substitui o elemento da posição 1 pelo 8 apenas na lista c
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print(f'Lista C: {c}')
