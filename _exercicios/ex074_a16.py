from random import randint
num = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(f'Os números sorteados formam: ')
for n in num:
    print(f'> {n}')
print('=' * 32)
print(f'O maior número sorteado foi: {max(num)}')
print(f'O menor número sorteado foi: {min(num)}')
