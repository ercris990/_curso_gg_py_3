print('{:=^60}'.format(' PAR OUU ÍMPAR '))
from random import randint
cont = 0
while True:
    pc = randint(1, 5)
    print('==' * 30)
    player = int(input('Diga o valor: '))
    resultado = pc + player
    opc = str(input('Par ou Ímpar [P/I]: ')).upper().strip()
    # while opc != 'P' or opc != 'I':
    #     opc = str(input('Digite [ P ] Par ou [ I ] - Ímpar '))
    print('==' * 30)
    # --------------------------------------------
    if opc == 'I' and resultado % 2 == 1:
        print('{:=^60}'.format(' Você VENCEU! '))
        print(f'o COMPUTADOR jogou {pc} e VOCÊ jogou {player}, o RESULTADO é {resultado} [ÍMPAR]')
        print('Joge novamente.')
    elif opc == 'P' and resultado % 2 == 0:
        print('{:=^60}'.format(' Você VENCEU! '))
        print(f'O COMPUTADOR jogou {pc} e VOCÊ jogou {player}, o RESULTADO e {resultado} [PAR]')
        print('Joge novamente.')
    else:
        print('GAME OVER!')
        break
    cont += 1
print('==' * 30)
if cont == 0:
    print('LAMENTO! Você não venceu nenhuma vez.')
elif cont == 1:
    print(f'Você venceu {cont} vez.')
else:
    print(f'Você venceu {cont} vezes.')
