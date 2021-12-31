num = int(input('Digite um número: '))

c = num
f = 1

print('Calculando \033[1;30m{}!\033[m = '.format(num), end='')

# Apague um para funcionar!

for c in range(num, 0, -1):
    print('\033[1;30m{}\033[m'.format(c), end='')
    print(' \033[1;31mx\033[m ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1 # #  #

print('\033[1;30m{}\033[m'.format(f))

while c > 0:
    print('\033[1;30m{}\033[m'.format(c), end='')
    print(' \033[1;31mx\033[m ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1

print('\033[1;30m{}\033[m'.format(f))
