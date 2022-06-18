from random import randint

computador = randint(0, 10)
tentativas = 0
jogador = 0

print('\033[1;36m''-=-''\033[m' * 15)
print('''\033[1;30mSou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?!\033[m''')
print('\033[1;36m''-=-''\033[m' * 15)
print()

while computador != jogador:
    jogador = int(input('Qual é seu palpite? '))
    tentativas += 1
    if jogador > computador:
        print('\033[31mMenos...\033[m Tente mais uma vez.')
        print()
    else:
        if jogador < computador:
            print('\033[32mMais...\033[m Tente mais uma vez.')
            print()
        if jogador == computador:
            print('\033[1;32mParabéns você acertou!\033[m')
            print()

print('Você precisou de \033[1;30m{}\033[m tentativas'.format(tentativas))
