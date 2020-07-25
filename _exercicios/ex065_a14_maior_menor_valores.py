media = cont = soma = maior = menor = 0
resposta = 'S'
while resposta in 'Ss':
    n = int(input('Digite um numero: '))
    cont += 1   # conta todos os números digitados pelo usuário
    soma += n   # soma todos os numeros digitados pelo usuários
    # verifica o maior e o menor valor digitado pelo usuário
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resposta = str(input('Quer continuar? [S|N] ')).upper().strip()
print('{:+^50}'.format(' RESULTADO '))
media = soma/cont                                                       # Calcula a média dos números digitados pelo usuário
print(f'Voce digitou {cont} numeros e a sua media foi {media:.1f}.')
print(f'O MENOR valor é o {menor} e o MAIOR valor é o {maior}.')
