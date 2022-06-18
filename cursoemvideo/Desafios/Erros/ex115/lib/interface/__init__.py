def menu(options: list):
    titulo('MENU PRINCIPAL')
    for i, v in enumerate(options):
        print(f'\033[33m{i + 1}\033[m - \033[36m{v}\033[m')
    print('-' * 42)
    opc = leiaInt('\033[33mSua Opção: \033[m')
    return opc


def titulo(msg: str, tam=42):
    from time import sleep
    print('-' * tam)
    print(f'{msg.center(tam)}')
    print('-' * tam)
    sleep(1)


def leiaInt(msg: str):
    import re
    val = input(msg)
    while not re.search(r'^-?\d+$', val):
        print(f'\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
        val = input(msg)
    return int(val)
