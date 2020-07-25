a = []
for c in range(0, 5):
    a.append(int(input(f'Digite um valor para a posição {c}: ')))
menor = min(a)
maior = max(a)
print('#' * 60)
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
