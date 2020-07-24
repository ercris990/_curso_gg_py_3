num = 0
while True:
    num = int(input('Digite um valor para ver a tabuada: '))
    print('_-_' * 13)
    if num <= 0:
        break
    for i in range(1, 11):
        print(f'{num} x {i} = {num * i}')
    print('=+=' * 13)
print('PROGRAMA TABUADA ENCERADO. Volte sempre!')
