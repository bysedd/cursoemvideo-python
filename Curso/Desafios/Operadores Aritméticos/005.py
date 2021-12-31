num = int(input('Digite um número: '))

print('Analisando o valor \033[1;30m{}\033[m, '
      'seu antecessor é \033[1;31m{}\033[m '
      'e o sucessor é \033[1;32m{}\033[m'.format(num, num - 1, num + 1))
