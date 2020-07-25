print('{:=^50}'.format(' ERMANNO SHOP '))
val_produto = float(input('Digite o valor do produto AKZ '))
print('{:=^50}'.format(' FORMAS DE PAGAMENTO '))
cond_pagamento = int(input(
    '1 - À vista [Dinheiro/Cheque]\n'
    '2 - À vista [Cartão]\n'
    '3 - Parcelado [2x no Cartão]\n'
    '4 - Parcelado [3x ou Mais no Cartão]\n'
    'Selecione um Opcção: '))
print('=' * 50)
print('Preço do Produto: AKZ {:.2f}'.format(val_produto))
if cond_pagamento == 1:
    print('Pagamento à Vista - Dinheiro/Cheque')
    print('Valor do Desconto: AKZ {:.2f} (10%)'.format((val_produto * 0.1)))
    print('Total a Pagar: AKZ {:.2f}'.format(val_produto - val_produto * 0.1))
elif cond_pagamento == 2:
    print('Pagamento à Vista - Cartão')
    print('Valor do Desconto: AKZ {:.2f} (5%)'.format((val_produto * 0.05)))
    print('Total a Pagar: AKZ {:.2f}'.format(val_produto - val_produto * 0.05))
elif cond_pagamento == 3:
    print('Pagamento Parcelado - Até 2x Cartão')
    print('Total a Pagar: AKZ {:.2f}'.format(val_produto))
    print('Valor por Parcela: AKZ {:.2f}'.format(val_produto / 2))
elif cond_pagamento == 4:
    print('Valor dos Juros: AKZ {:.2f}'.format(val_produto * 0.2))
    print('Total a Pagar: AKZ {:.2f}'.format(val_produto + (val_produto * 0.2)))
    print('=' * 50)
    num_parcela = int(input('Nº de Parcelas: '))
    print('=' * 50)
    if num_parcela <= 2:
        print('Pagamento Parcelado - Até 2x Cartão')
        print('Total a Pagar: AKZ {:.2f}'.format(val_produto))
        print('Valor por Parcela: AKZ {:.2f}'.format(val_produto / num_parcela))
    else:
        print('Pagamento Parcelado - 3x ou Mais no Cartão')
        print('Valor dos Juros: AKZ {:.2f} (20%)'.format((val_produto * 0.2)))
        print('Nº de Parcelas: {}'.format(num_parcela))
        print('Total a Pagar: AKZ {:.2f}'.format((val_produto + val_produto * 0.2)))
        print('Valor por Parcela: AKZ {:.2f}'.format((val_produto + val_produto * 0.20) / num_parcela))
else:
    print('Opcção inválida, tente novamente!')
print('=' * 50)
print('\nOBRIGADO, Volte Sempre!')
