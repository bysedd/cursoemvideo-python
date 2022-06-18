from random import randint

computador = randint(0, 10)
v = 0

print('\033[1;30m=-\033[m' * 13)
print('\033[1;36mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('\033[1;30m=-\033[m' * 13)

while True:
    jogador = int(input('\033[1;36mDiga um valor: \033[m'))
    total = jogador + computador
    computador = randint(0, 10)
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('\033[1;36mPar ou Ímpar?\033[m [\033[1;33mP\033[m/\033[1;34mI\033[m] ')).strip().upper()[0]
    print('\033[1;30m--\033[m' * 13)
    print(f'\033[1;36mVocê jogou {jogador} e o computador {computador}. Total de {total}\033[m ', end='')
    print('\033[1;33mDEU PAR\033[m' if total % 2 == 0 else '\033[1;34mDEU ÍMPAR\033[m')
    print('\033[1;30m--\033[m' * 13)
    if tipo == 'P':
        if total % 2 == 0:
            print('\033[1;32mVocê VENCEU!\033[m')
            v += 1
        else:
            print('\033[1;31mVocê PERDEU!\033[m')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('\033[1;32mVocê VENCEU!\033[m')
            v += 1
        else:
            print('\033[1;31mVocê PERDEU!\033[m')
            break
    print('\033[1;30mVamos jogar novamente...\033[m')
    print('\033[1;30m=-\033[m' * 13)
print('\033[1;30m=-\033[m' * 13)
print(f'\033[1;31mGAME OVER!\033[m \033[1;36mVocê venceu {v} vezes.\033[m')
