from random import choice
from time import sleep
print('{:=^40}'.format(' JOGO - JOKEN PO '))
pc = choice(['Pedra', 'Papel', 'Tesoura'])
player = int(input('=== OPÇÕES ===\n'
                   '1. Pedra\n'
                   '2. Papel\n'
                   '3. Tesoura\n'
                   'Selencione uma opção: '))
# ----------------------------------------------------------------------------------------------------------------------
print('=' * 40)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
# ----------------------------------------------------------------------------------------------------------------------
if player == 1:
    player = 'Pedra'
    print('Player: {}'.format(player))
    print('Computador: {}'.format(pc))
    if pc == 'Papel':
        print('Você PERDEU!')
    elif pc == 'Tesoura':
        print('Você GANHOU!')
    else:
        print('> Jogo EMPATADO!\n'
              '> Tente novamente!')
# ----------------------------------------------------------------------------------------------------------------------
elif player == 2:
    player = 'Papel'
    print('Player: {}'.format(player))
    print('Computador: {}'.format(pc))
    if pc == 'Tesoura':
        print('Você PERDEU!')
    elif pc == 'Pedra':
        print('Você GANHOU!')
    else:
        print('> Jogo EMPATADO!\n'
              '> Tente Novamente!')
# ----------------------------------------------------------------------------------------------------------------------
elif player == 3:
    player = 'Tesoura'
    print('Player: {}'.format(player))
    print('Computador: {}'.format(pc))
    if pc == 'Papel':
        print('Você PERDEU!')
    elif pc == 'Pedra':
        print('Você GANHOU!')
    else:
        print('> Jogo EMPTADO!\n'
              '> Tente Novamente!')
# ----------------------------------------------------------------------------------------------------------------------
else:
    print('Tente novamente!\n'
          'Digite uma opção entre 1 a 3.')
print('=' * 40)
