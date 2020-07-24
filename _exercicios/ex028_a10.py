from random import randint
from time import sleep
aleatorio = randint(0, 5)
num = int(input('Digite um numero: '))
print('PROCESSANDO...')
sleep(2)
if aleatorio == num:
    print('PARABENS, voce acertou!')
else:
    print('LAMENTO, tente mais uma vez!')
print('-> Numero aleatorio: {}'.format(aleatorio))
print('-> Sua tentativa: {}'.format(num))
