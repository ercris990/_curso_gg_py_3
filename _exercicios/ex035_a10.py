r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
print('=' * 30)
if ((r1+r2) > r3) and ((r2+r3) > r1) and ((r3+r1) > r2):
    print('É possível formar um triangulo.')
else:
    print('NÂO É possível formar um triângulo.')
print('=' * 30)
