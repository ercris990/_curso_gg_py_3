numlist = []

while True:
    num = int(input('Digite um numero: '))
    opc = str(input('Deseja continuar S|N: ')).strip().upper()
    if opc not in 'SsNn':
        opc = str(
            input('Digite [S] para continuar e [N] para parar: ')).strip().upper()
    if opc in 'Nn':
        break
    numlist.append(num)
print(f'Os valores digitados foram: {numlist}')
