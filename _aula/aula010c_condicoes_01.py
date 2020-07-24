n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('-----------------------')
print('1ª Nota: {}'.format(n1))
print('2ª Nota: {}'.format(n2))
if m >= 5:
    print('-> Media: {:.1f}\nvoce foi APROVADO\n-- PARABENS! --'.format(m))
else:
    print('-> Media: {:.1f}\nVoce foi REPROVADO\n-- ESUDE MAIS! --'.format(m))
