s = 0

for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n

print()
print('A soma de todos os valores foi \033[1;30m{}\033[m.'.format(s))
