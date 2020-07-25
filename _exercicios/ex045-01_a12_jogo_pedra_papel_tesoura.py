from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
# ----------------------------------------------------------------------------------------------------------------------
print('''Suas Opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('Qual é a sua jogada: '))
print('=+=' * 8)
print('Computador jogou: {}'.format(itens[pc]))
print('Jogador jogou: {}'.format(itens[player]))
print('=+=' * 8)
