listNum = []
while True:
    num = int(input('Digite um valor: '))
    if num not in listNum:
        listNum.append(num)
        print('Valor adicionado com SUCESSO...')
    else:
        print('Número DUPLICADO! Digite outro número por favor.')
    opc = str(input('Deseja continuar [S/N]: ')).upper().strip()
    while opc not in 'SsNs':
        opc = str(
            input('Digite [S] para continuar e [N] para parar: ')).upper().strip()
    if opc in 'N':
        break
print('=+=' * 16)
print(f'Voce digitou os valores {sorted(listNum)}')
