from math import trunc

num = float(input('Digite um valor: '))

print('O valor digitado foi \033[1;30m{}\033[m e a sua porção inteira é \033[1;30m{}\033[m'.format(num, trunc(num)))
