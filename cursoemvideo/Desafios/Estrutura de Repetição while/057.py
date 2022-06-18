sexo = str(input('Informe seu sexo: ')).strip().upper()[0]

while sexo not in 'MF':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]

print('Sexo \033[1;30m{}\033[m registrado com \033[1;32msucesso\033[m'.format(sexo))
