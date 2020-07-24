n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
media = (n1 + n2) / 2
print('=+=' * 10)
print('Nota 1: {:.1f} valores.'.format(n1))
print('Nota 2: {:.1f} valores.'.format(n2))
print('Média: {:.1f} valores.'.format(media))
print('=+=' * 10)
if 0 < media < 5:
    print('Resultado: Reprovado.')
elif 5 <= media <= 6.9:
    print('Resultado: Recuperação.')
elif 7 <= media <= 10:
    print('Resultado: Aprovado.')
print('=+=' * 10)
