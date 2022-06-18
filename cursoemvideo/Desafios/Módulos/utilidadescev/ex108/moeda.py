def metade(price=0.0):
    return price / 2


def dobro(price=0.0):
    return price * 2


def aumentar(price=0.0, porcem=0):
    return price + porcem / 100 * price


def diminuir(price=0.0, porcem=0):
    return price - porcem / 100 * price


def moeda(price=0.0, value='R$'):
    return f'{value}{price:.2f}'.replace('.', ',')
