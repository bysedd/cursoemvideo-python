algo = input('Digite algo: ')

print('O tipo primitivo desse valor é \033[1;30m{}\033[m'.format(type(algo)))
print('Só tem espaços? \033[1;30m{}\033[m'.format(algo.isspace()))
print('É um número? \033[1;30m{}\033[m'.format(algo.isnumeric()))
print('É alfabético? \033[1;30m{}\033[m'.format(algo.isalpha()))
print('É alfanúmerico? \033[1;30m{}\033[m'.format(algo.isalnum()))
print('Está em maíusculas? \033[1;30m{}\033[m'.format(algo.isupper()))
print('Está em minúsculas? \033[1;30m{}\033[m'.format(algo.islower()))
print('Está capitalizada? \033[1;30m{}\033[m'.format(algo.istitle()))
