import random
n_dig = int(input('Digite um numero: '))
n_ale = random.randint(0, 10)

if(n_dig > 0 and n_dig <= 10):
    if(n_dig == n_ale):
        print('{} e igual a {}'.format(n_dig, n_ale))
        print('Parabens, voce ACERTTOU!')
    else:
        print('{} e diferente de {}'.format(n_dig, n_ale))
        print('Lamento, voce ERROU!')
else:
    n_dig = int(input('Digite um numero maior que 0 e menor ou igual a 10: '))
