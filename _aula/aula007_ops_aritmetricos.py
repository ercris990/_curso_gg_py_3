# operações aritméticas
n1 = int(input('Digite o 1º numero: '))
n2 = int(input('Digite 0 2º numero: '))
# ---------------------------------
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# ---------------------------------
print('-----------------------------------')
print('- a soma é: {}, - o produto é: {}, - a divisão é: {:.2f} '.format(s, m, d), end='')
print('- a divisão inteira é: {}, - a potencia é: {}'.format(di, e))
