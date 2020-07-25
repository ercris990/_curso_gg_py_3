listagem = ('Monitor', 35000.74, 'Mouse', 1532.56, 'Teclado', 2300,
            'Impressora', 73209, 'Cabo USB', 790.99, 'Pendrive', 1705.1)
print('=' * 60)
print(f'{"LISTAGEM DE COMPRAS":^60}')
print('=' * 60)
for position in range(0, len(listagem)):
    if position % 2 == 0:
        print(f'{position + 1}. {listagem[position]:.<40}', end='')
    else:
        print(f'AOA {listagem[position]:>8.2f}')
print('=' * 60)
