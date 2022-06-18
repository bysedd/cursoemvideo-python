import re


def isfloat(val):
    if isinstance(val, float):
        return True
    if re.search(r'^-?\d+\.\d+$', val):
        return True
    return False


def isint(val):
    if isinstance(val, int):
        return True
    if re.search(r'^-?\d+$', val):
        return True
    return False


def isnumber(val):
    return isint(val) or isfloat(val)


def leiaDinheiro(msg: str):
    val = input(msg).strip().replace(',', '.')
    while not isnumber(val):
        print(f'\033[1;31mERRO: "{val}" é um preço inválido!\033[m')
        val = input(msg).strip().replace(',', '.')
    return float(val)
