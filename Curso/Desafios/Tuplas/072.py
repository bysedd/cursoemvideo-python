cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
        'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
while True:
    número = int(input('Digite um número entre 0 e 20: '))
    if 0 <= número <= 20:
        resp = str(input('Você quer continuar? [S/N] ')).strip().upper()
        if resp == 'S':
            número = int(input('Digite um número entre 0 e 20: '))
        else:
            break
    print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[número]}')
