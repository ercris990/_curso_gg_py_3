qtdProdutos = valCompra = mais1000 = maisBarato = 0
nomeMaisbarato = ''
while True:
    nomeProduto = str(input('Digite o nome do produto: '))
    precoProduto = float(input('Digite o preço do produto: AOA '))
    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja adicionar produto? [S|N]: ')).upper()[0].strip()
    # --------------------------------------------------------------------------
    qtdProdutos += 1                          # calcula a quantidade de produtos
    valCompra += precoProduto                 # calcula o valor total da compra
    # mostra os produtos que custam mais de AOA 1000
    if precoProduto > 1000:
        mais1000 += 1
    # mostra o nome e o preço do produto mais barato
    if qtdProdutos == 1 or precoProduto < maisBarato:
        maisBarato = precoProduto
        nomeMaisbarato = nomeProduto
    # --------------------------------------------------------------------------
    if opc == 'N':
        break
print('{:=^40}'.format(' RESUMO DA FATURA '))
print(f'> Quantidade de produtos: {qtdProdutos}')
print(f'> Valor total da compra: {valCompra:.2f}')
print(f'> {mais1000} prodtos custam mais de AOA 1000.')
print(f'> O produto mais barato é o(a) {nomeMaisbarato} e custa AOA {maisBarato:.2f}')
print('{:=^40}'.format(' OBRIGADO! Volte Sempre! '))
