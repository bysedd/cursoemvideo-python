num = int(input('Digite um número: '))

print('O dobro de \033[1;30m{}\033[m vale \033[32m{}\033[m.'.format(num, num * 2))
print('O triplo de \033[1;30m{}\033[m vale \033[1;32m{}\033[m.'.format(num, num * 3))
print('A raiz quadrada de \033[1;30m{}\033[m é igual a \033[7;30;32m{:.2f}\033[m.'.format(num, num ** (1 / 2)))
