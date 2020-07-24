num = int(input('Digite um número: '))
total = 0
print('=' * 40)
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mVoce digitou: {}'.format(num))
print('\033[mO numero {} foi divisível por {} vezes'.format(num, total))
if total == 2:
        print('\033[33mO número {} É UM NUMERO PRIMO.'.format(num))
else:
    print('\033[31mO número {} NÃO É UM NÚMERO PRIMO.'.format(num))
