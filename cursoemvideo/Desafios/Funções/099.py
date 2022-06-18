from time import sleep


def maior(*num):
    print(f'{"-=" * 30}\n'
          f'Analisando os valores passados...')
    for n in num:
        print(n, end=' ')
        sleep(0.3)
    print(f'Foram informados {len(num)} valores ao todo.')
    if len(num) > 0:
        print(f'O maior valor informado foi {max(num)}.')
    else:
        print(f'O maior valor informado foi 0.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
