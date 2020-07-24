from math import factorial
num = int(input('Digite um número para\nCalcular o seu Fatorial: '))
print('{:=^156}'.format(' CALCULO DE FATORIAL - UTILIZANDO O MÓDULO [MATH] '))
fatorial = factorial(num)
print('Calculando {}! = {}'.format(num, fatorial))
# --------------------------------------------------------------------------
print('{:=^156}'.format(' CALCULO DE FATORIAL - UTILIZANDO WHILE '))
c = num
f = 1
print('Calculando {}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
