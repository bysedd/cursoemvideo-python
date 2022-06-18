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


def resumo(price: float, aum: int, red: int):
    """
    -> Mostra o resumo usando todas as outras funções.

    :param price: Preço.
    :param aum: % de aumento.
    :param red: % de redução.
    :return: Sem retorno.
    """
    print(f"{'-' * 30}\n"
          f"{'RESUMO DO VALOR'.center(30)}\n"
          f"{f'-' * 30}")
    print(f"Preço analisado: \t{moeda(price)}\n"
          f"Dobro do preço: \t{dobro(price, True)}\n"
          f"Metade do preço: \t{metade(price, True)}\n"
          f"{aum}% de aumento: \t{aumentar(price, aum, True)}\n"
          f"{red}% de redução: \t{diminuir(price, red, True)}")
