from random import choice
from time import sleep

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada = int(input('Qual é a sua jogada? '))
itens = 'Pedra', 'Papel', 'Tesoura'
computador = choice(itens)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('\033[1;30m''-=-''\033[m' * 8)
print('Computador jogou \033[1;30m{}\033[m'.format(computador))

if jogada == 0:
    print('Jogador jogou \033[1;30mPedra\033[m')
    print('\033[1;30m''-=-''\033[m' * 8)
    if computador == 'Pedra':
        print('\033[1;30mEMPATE\033[m')
    elif computador == 'Tesoura':
        print('\033[1;32mJOGADOR VENCE\033[m')
    elif computador == 'Papel':
        print('\033[1;31mJOGADOR PERDE\033[m')
if jogada == 1:
    print('Jogador jogou \033[1;30mPapel\033[m')
    print('\033[1;30m''-=-''\033[m' * 8)
    if computador == 'Pedra':
        print('\033[1;32mJOGADOR VENCE\033[m')
    elif computador == 'Tesoura':
        print('\033[1;31mJOGADOR PERDE\033[m')
    elif computador == 'Papel':
        print('\033[1;30mEMPATE\033[m')
if jogada == 2:
    print('Jogador jogou \033[1;30mTesoura\033[m')
    print('\033[1;30m''-=-''\033[m' * 8)
    if computador == 'Pedra':
        print('\033[1;31mJOGADOR PERDE\033[m')
    elif computador == 'Tesoura':
        print('\033[1;30mEMPATE\033[m')
    elif computador == 'Papel':
        print('\033[1;32mJOGADOR VENCE\033[m')
elif jogada >= 3:
    print('\033[1;30m''-=-''\033[m' * 8)
    print('\033[1;31mJOGADA INVÁLIDA\033[m')
