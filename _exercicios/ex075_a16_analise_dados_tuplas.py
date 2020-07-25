num = (int(input('Digite um numero: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print('=-=' * 20)
print(f'>> Você digitou os seguintes valores: {num}')
print('=-=' * 20)
print(f'Ordem crescente: {sorted(num)}.')
print(f'O número 9 aparece {num.count(9)} vez(es).')
if 3 in num:
    print(f'O primeiro número 3 encontra-se na {num.index(3) + 1}ª posição.')
else:
    print('O número 3 não foi digitado em nenhuma posição.')
print('Os números pares forma: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
