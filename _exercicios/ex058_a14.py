from random import randint
pc = randint(0, 10)
cont = 0
print("""Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que voce consegue adivinhar qual foi? """)
num = int(input('Qual é o seu palpite?\n-> '))
while num != pc:
    num = int(input('Tente novamente: '))
    cont += 1
print('=+=' * 10)
print('Parabéns, você ACERTOU!!!')
print('Nº de tentativas: {}'.format(cont+1))
print('Palpite do PC: {}'.format(pc))
print('Seu Palpite: {}'.format(num))
