numList = []
cont = 0
while True:
    numList.append(int(input('Digite um Valor: ')))
    cont += 1
    opc = str(input('Deseja Continuar? [S/N] ')).upper().strip()
    while opc not in 'SsNn':
        opc = str(input('Digite [S] para continuar e [N] para parar: '))
    if opc == 'N':
        break
print('=+=' * 20)
print(f'Você digitou ao todo {cont} valores')                   #opção 01
print(f'Você digitou ao todo {len(numList)} valores')           #opção 02
print(f'Voce digitou os seguintes valores {numList}')
numList.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {numList}')
if 5 in numList:
    print(f'O valor 5 FAZ parte da lista e encontra-se na posição {numList.index(5)}.')
else:
    print('O valor NÃO foi encontrado na lista.')
