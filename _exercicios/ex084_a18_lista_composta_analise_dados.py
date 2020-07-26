temp = list()
principal = list()
menorpeso = maiorpeso = 0
print('=-=' * 25)
while True:
    temp.append(str(input('Nome: ')).strip().title())
    temp.append(float(input('Peso: ')))
    if len(principal) == 0:
        maiorpeso = menorpeso = temp[1]
    else:
        if temp[1] > maiorpeso:
            maiorpeso = temp[1]
        if temp[1] < menorpeso:
            menorpeso = temp[1]
    principal.append(temp[:])
    temp.clear()
    opc = str(input('Deseja continuar S/N: ')).strip().capitalize()
    while opc not in 'SsNn':
        opc = str(input('Digite S para continuar e N para parar: '))
    if opc in 'Nn':
        break

print('=-=' * 25)
print(f'Foram cadastradas {len(principal)} pessoas.')
print(f'Os maior peso foi {maiorpeso}Kg.')
for p in principal:
    if p[1] == maiorpeso:
        print(f'> {p[0]}')
print(f'Os menor peso foi {menorpeso}Kg.')
for p in principal:
    if p[1] == menorpeso:
        print(f'> {p[0]}')
print('=-=' * 25)
