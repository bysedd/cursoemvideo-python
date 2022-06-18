print('\033[1;36m=\033[m' * 25)
print('     \033[1;30mGerador de PA\033[m     ')
print('\033[1;36m=\033[m' * 25)

primeiro = int(input('\033[1;30mPrimeiro termo:\033[m '))
razão = int(input('\033[1;30mRazão da PA:\033[m '))

termo = primeiro
cont = 1

while cont <= 10:
    print('\033[1;30m{}\033[m'.format(termo), end='')
    print(' -> ' if cont < 10 else ' -> \033[1;31mFIM\033[m ', end='')
    termo += razão
    cont += 1
