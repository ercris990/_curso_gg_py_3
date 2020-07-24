n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
print('=' * 23)
print('1º valor: {}'.format(n1))
print('2º valor: {}'.format(n2))
print('=' * 23)
if n1 > n2:
    print('O 1º valor é o maior.')
elif n2 > n1:
    print('O 2º valor é o maior.')
else:
    print('Não existe valor maior.\nOs 2 são iguais.')
