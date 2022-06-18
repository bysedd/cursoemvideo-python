def leiaFloat(msg: str):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[1;31mERRO: por favor, digite um número real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[1;31mUsuário preferiu não digitar esse número.\033[m')
            return 0.0
        else:
            return float(n)


def leiaInt(msg: str):
    import re
    try:
        val = input(msg)
        while not re.search(r'^-?\d+$', val):
            print(f'\033[1;31mERRO: por favor, digite um número inteiro válido.\033[m')
            val = input(msg)
        return int(val)
    except KeyboardInterrupt:
        print('\n\033[1;31mUsuário preferiu não digitar esse número.\033[m')
        return 0
