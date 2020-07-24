n = input('Digite um valor: ')
print(type(n))  # verifica o tipo primitivo
print('Número: ', n.isnumeric())
print('Alfabeto: ', n.isalpha())
print('Alfanumerico: ', n.isalnum())
print('Decimal: ', n.isdecimal())
