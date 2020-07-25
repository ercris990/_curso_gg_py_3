numList = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > numList[-1]:
        numList.append(num)
        print('Valor adicionado no final da lista...')
    else:
        posicao = 0
        while posicao < len(numList):
            if num <= numList[posicao]:
                numList.insert(posicao, num)
                print(f'Valor adicionado na posição {posicao}...')
                break
            posicao += 1
print('=+=' * 18)
print(f'>>> Você digitou os seguintes valores: {numList}')
