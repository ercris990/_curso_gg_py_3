r1 = float(input('Digite o 1º segmento: '))
r2 = float(input('Digite o 2º segmento: '))
r3 = float(input('Digite o 3º segmento: '))
print('=+=' * 20)
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    if r1 == r2 == r3:
        print('Forma um Triângulo EQUILÁTERO (todos os lados iguais).')
    elif r1 != r2 != r3 != r1:
        print('Forma um Triângulo ESCALENO (todos os lados diferentes).')
    else:
        print('Forma um Triangulo ISÓSCELES (apenas dois lados iguais).')
else:
    print('NÂO Forma Triâgulo.')
print('=+=' * 20)
