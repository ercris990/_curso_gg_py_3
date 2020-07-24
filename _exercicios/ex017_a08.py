# Cal;culo da Hipotenusa [Modulos]
from math import hypot
co = float(input('Comprimento do Cateto Oposto: '))
ca = float(input('Comprimento do Cateto Adjacente: '))
hi = hypot(co, ca)
print('--------------------------------')
print('A Hipotenusa vai medir {:.2f}'.format(hi))
