num = int(input('Digite um número para ver a sua tabuada: '))
for i in range(1, 11):
    print('{} x {:2} = {}'. format(num, i, num * i))
