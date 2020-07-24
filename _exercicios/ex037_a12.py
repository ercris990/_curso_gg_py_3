num = int(input('Digite um numero inteiro: '))
opcao = int(input('Qual a sua opção:\n'
                  '1. Binário;\n'
                  '2. Octal;\n'
                  '3. Hexadecimal\n'
                  'Digite uma Opção: '))
print('=+=' * 30)
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a:{}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a: {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a: {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')
print('=+=' * 30)
