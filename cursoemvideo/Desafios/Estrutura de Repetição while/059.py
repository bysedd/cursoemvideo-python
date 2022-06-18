from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
maior = 0
escolha = 0

while escolha != 5:
    print('''\033[1;30m--------------- MENU ---------------\033[m
Os números registrados são \033[1;30m{}\033[m e \033[1;30m{}\033[m
\033[1;32m[ 1 ] somar\033[m
\033[1;33m[ 2 ] multiplicar\033[m
\033[1;36m[ 3 ] maior\033[m
\033[1;35m[ 4 ] novos números\033[m
\033[1;31m[ 5 ] sair do programa\033[m'''.format(n1, n2))
    print()
    escolha = int(input('\033[1;30m>>>>> Escolha uma opção:\033[m '))
    if escolha == 1:
        print('A soma entre \033[1;30m{}\033[m + \033[1;30m{}\033[m é \033[1;32m{}\033[m'.format(n1, n2, n1 + n2))
        print('\033[1;30m''=-=''\033[m' * 10)
        sleep(2)
    if escolha == 2:
        print('O resultado de \033[1;30m{}\033[m x \033[1;30m{}\033[m é \033[1;33m{}\033[m'.format(n1, n2, n1 * n2))
        print('\033[1;30m''=-=''\033[m' * 10)
        sleep(2)
    if escolha == 3:
        if maior == 1:
            maior = n1
        else:
            if maior < n1:
                maior = n1
            else:
                maior = n2
        print('Entre \033[1;30m{}\033[m e \033[1;30m{}\033[m o maior valor é \033[1;36m{}\033[m'.format(n1, n2, maior))
        print('\033[1;30m''=-=''\033[m' * 10)
        sleep(2)
    if escolha == 4:
        print('\033[1;35mInforme os números novamente...\033[m')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('\033[1;30m''=-=''\033[m' * 10)
        sleep(2)
    if escolha == 5:
        print('\033[1;31mFinalizando...\033[m')
        print('\033[1;30m''=-=''\033[m' * 10)
        sleep(2)
        print('\033[1;30mFim do programa! Volte sempre!\033[m')
    if escolha >= 6:
        print('\033[1;31mOpção inválida!\033[m')
        print('\033[1;30m''=-=''\033[m' * 10)
        sleep(2)
