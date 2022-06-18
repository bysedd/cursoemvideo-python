palavra = ('APRENDER',
           'PROGRAMAR',
           'LINGUAGEM',
           'PYTHON',
           'CURSO',
           'FREE',
           'ESTUDAR',
           'PRATICAR',
           'TRABALHAR',
           'MERCADO',
           'PROGRAMADOR',
           'TRADING')
for p in palavra:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
