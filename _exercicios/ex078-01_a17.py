a = []
menor = 0
maior = 0
for c in range(0, 5):
    a.append(int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        menor = maior = a[c]
    else:
        if a[c] < menor:
            menor = a[c]
        if a[c] > maior:
            maior = a[c]
print('#' * 70)
print(f'Lista: {a}')
print(f'O menor valor da lista é {menor} e está nas posições ', end='')
for i, v in enumerate(a):
    if v == menor:
        print(f'{i}... ', end='')
print()
print(f'O maior valor da lista é {maior} e está nas posições ', end='')
for i, v in enumerate(a):
    if v == maior:
        print(f'{i}... ', end='')
print()
