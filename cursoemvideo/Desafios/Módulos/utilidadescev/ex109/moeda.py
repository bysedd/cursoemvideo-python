def metade(price: float, formatar=False):
    """
    -> Retorna a metade do preço.

    :param price: Preço.
    :param formatar: Formatar resultado para uma mensagem.
    :return: Mensagem formatada ou apenas o resultado.
    """
    res = price / 2
    return res if not formatar else moeda(res)


def dobro(price: float, formatar=False):
    """
    -> Retorna o dobra o preço.

    :param price: Preço.
    :param formatar: Formatar resultado para uma mensagem.
    :return: Mensagem formatada ou apenas o resultado.
    """
    res = price * 2
    return res if not formatar else moeda(res)


def aumentar(price: float, porcem: int, formatar=False):
    """
    -> Retorna o aumento do preço por meio de uma porcentagem.

    :param price: Preço.
    :param porcem: Porcentagem.
    :param formatar: Formatar resultado para uma mensagem.
    :return: Mensagem formatada ou apenas o resultado.
    """
    res = price + (porcem / 100 * price)
    return res if formatar is False else moeda(res)


def diminuir(price: float, porcem: int, formatar=False):
    """
    -> Retorna a redução do preço por meio de uma porcentagem.

    :param price: Preço.
    :param porcem: Porcentagem.
    :param formatar: Formatar resultado para uma mensagem.
    :return: Mensagem formatada ou apenas o resultado.
    """
    res = price - (porcem / 100 * price)
    return res if not formatar else moeda(res)


def moeda(price: float):
    """
    -> Retorna o preço em uma mensagem.

    :param price: Preço.
    :return: Uma string.
    """
    return f'R${price:.2f}'.replace('.', ',')
