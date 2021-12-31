nome = str(input('Qual é o seu nome? '))

if nome == 'Felippe':
    print('Que nome bonito você tem!')
elif nome == 'Pedro':
    print('Macaco')
elif nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é bem normal.')

print('Tenha um bom dia, {}!'.format(nome))
