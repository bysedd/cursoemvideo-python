a = 3
b = 5

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;30m'}

print('Os valores são \033[34m{}\033[m e \033[33m{}\033[m!'.format(a, b))
print('Os valores são {}{}{} e {}{}{}!'.format('\033[34m', a, '\033[m', '\033[33m', b, '\033[m'))
print('Os valores são {}{}{} e {}{}{}!'.format(cores['azul'], a, cores['limpa'], cores['amarelo'], b, cores['limpa']))
