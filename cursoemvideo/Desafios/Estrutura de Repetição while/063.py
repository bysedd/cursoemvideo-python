print('\033[1;30m-\033[m' * 30)
print(' \033[1;36mSequência de Finobacci\033[m')
print('\033[1;30m-\033[m' * 30)

termos = int(input('Quantos termos você quer mostrar? '))
print('\033[1;30m~\033[m' * 30)

t1 = 0
t2 = 1

print('\033[1;30m{}\033[m -> \033[1;30m{}\033[m'.format(t1, t2), end='')

cont = 3

while cont <= termos:
    t3 = t1 + t2
    print(' -> \033[1;30m{}\033[m'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1

print(' -> \033[1;31mFIM\033[m')
