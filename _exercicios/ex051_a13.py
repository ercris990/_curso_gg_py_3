primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
pa = primeiro + (10 - 1) * razao
for i in range(primeiro, pa + razao, razao):
    print('{} '.format(i), end='-> ')
print('FINISH!')
