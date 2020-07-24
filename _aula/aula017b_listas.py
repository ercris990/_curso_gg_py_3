valores = list(range(5, 11))        # também funciona com a função tuple
print(f'Primeira Lista: {valores}')
print('===' * 15)
valores = [3, 0, 1, 8, 2, 8, 7]
print(f'Segunda lista: {valores}')
print('===' * 15)
valores.append(10)              # adiciona o número 10 no final da lista
print(valores)
valores.sort()                  # organiza os elementos da lista em ordem crescente
print(valores)
valores.sort(reverse=True)      # organiza o elementos da lista em ordem decrescente
print(valores)
print(f'Essa lista tem {len(valores)} elementos.')      # mostra o números de elementos da lista
valores.insert(2, 99)   # adiciona o número 99 na posição 1
print(valores)
valores.pop()           # elimina o último elemento da lista
print(valores)
valores.remove(99)      # elimina o número 99 da lista
print(valores)
if 100 in valores:      # remove o numero 100 da lista caso ele exista
    valores.remove(100)
else:
    print('! O número 100 não se encontra nesta lista.')
