from time import sleep


def lin():
    print('-=' * 30)


def contagem(i, f, p):
    lin()
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        sleep(2.5)
        for c in range(i, f + 1, p):
            sleep(0.5)
            print(c, end=' ')
        print('FIM!')
    else:
        sleep(2.5)
        p *= -1
        for c in range(i, f - 1, p):
            sleep(0.5)
            print(c, end=' ')
        print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)
lin()
print('Agora é a sua vez de personalizar a contagem!')
contagem(int(input('Início: ')), int(input('Fim:\t')), int(input('Passo:  ')))
