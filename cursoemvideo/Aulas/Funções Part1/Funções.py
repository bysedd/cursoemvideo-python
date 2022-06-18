def titulo(txt: str):
    print(f"{'-' * (len(txt) * 2)}\n{txt:^{len(txt) * 2}}\n{'-' * (len(txt) * 2)}")


def soma(*num: int):
    print(f'A soma dos números {num} é {sum(num)}.')


def contador(*num: int):
    print(f'Recebi {len(num)} números.\n'
          f'São eles: {num}\n')


def dobra(lista: list):
    print(f'{lista} ==> ', end='')
    for i, _ in enumerate(lista):
        lista[i] *= 2
    print(lista)


titulo('CURSO EM VÍDEO')
titulo('PYTHON É MUITO BOM!')
titulo('Oi')

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

dobra([7, 2, 5, 0, 4])
dobra([6, 3, 9, 1, 0, 2])

soma(5, 2, 6, 9, 1, 3, 7)
