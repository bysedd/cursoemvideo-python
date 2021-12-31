print('\033[1;36m=\033[m' * 25)
print('     \033[1;30mGerador de PA\033[m     ')
print('\033[1;36m=\033[m' * 25)

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))

termo = primeiro
cont = 1
total = 0
pausa = 10

while pausa != 0:
    total += pausa
    while cont <= total:
        print('\033[1;30m{}\033[m -> '.format(termo), end='')
        termo += razão
        cont += 1
    print('\033[1;32mPausa\033[m')
    pausa = int(input('Quantos termos você quer mostrar a mais? '))
    if pausa == 0:
        print('\033[1;31mProgressão finalizada\033[m com \033[1;30m{} termos\033[m mostrados.'.format(cont - 1))
