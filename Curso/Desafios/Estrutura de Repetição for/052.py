num = int(input('Digite um número: '))

tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        print('\033[1;32m', end='')
        tot += 1
    else:
        print('\033[1;31m', end='')
    print('{}'.format(c), end=' ')

print()
print('\033[mO número \033[1;30m{}\033[m foi divisível \033[1;30m{}\033[m vezes.'.format(num, tot))

if tot > 2:
    print('E por isso ele \033[1;31mNÃO É PRIMO!\033[m')
else:
    print('E por isso ele \033[1;32mÉ PRIMO!\033[m')
