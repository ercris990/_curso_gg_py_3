n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
opc = 0
while opc != 5:
    print("""========== OPÇÕES ========== 
    [ 1 ] Somar
    [ 3 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos Números
    [ 5 ] Sair do Programa\n============================""")
    opc = int(input('Digite a sua opção: '))
    if opc == 1:
        soma = n1 + n2
        print('Resultado: A soma de {} + {} = {}'.format(n1, n2, soma))
    elif opc == 2:
        produto = n1 * n2
        print('Resultado: A multiplicação de {} x {} = {}'.format(n1, n2, produto))
    elif opc == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior valor é: {}'.format(n1, n2, maior))
        elif n1 < n2:
            maior = n2
            print('Entre {} e {} o maior valor é: {}'.format(n1, n2, maior))
        else:
            print('Os dois numeros são iguais.')
    elif opc == 4:
        print('Digite novamente')
        n1 = int(input('Primeiro numero: '))
        n2 = int(input('Segundo numero: '))
    elif opc >= 6:
        print('Opcao inválida!')
print('Fim do programa!')
