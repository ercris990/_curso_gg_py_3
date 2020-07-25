a = float(input('Qual a altura da parede: '))
l = float(input('Qual a largura da parede: '))
ar = (a*l)
qt = (ar/2)
print('---------------------------------------------------')
print('A Altura da parede é de: {:.2f} metros\nA Largura da pared é de {:.2f} metros\nA Área da parede é de {:.2f} metros ao quadrado:'.format(
    a, l, ar))
print(
    'Será necessário {:.2f} litros de tinta para pintar a parede.'.format(qt))
