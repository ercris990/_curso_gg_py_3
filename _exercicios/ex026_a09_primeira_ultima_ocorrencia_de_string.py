frase = str(input('Digite uma frase: ')).upper().strip()
print('A frase digiteda e: {}'.format(frase))
print('A palavra a aparece {} vezes'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('A')+1))

