def metade(price: float, formatar=False):
    """
    -> Calcula a metade de um determinado preço,
    retornando o resultado com ou sem formatação.

    :param price: o preço que se quer dividir.
    :param formatar: quer a saída formatada ou não?
    :return: o valor dividido, com ou sem formatação.
    """
    res = price / 2
    return res if not formatar else moeda(res)


def dobro(price: float, formatar=False):
    """
    -> Calcula o dobro de um determinado preço,
    retornando o resultado com ou sem formatação.

    :param price: o preço que se quer dobrar.
    :param formatar: quer a saída formatada ou não?
    :return: o valor dobrado, com ou sem formatação.
    """
    res = price * 2
    return res if not formatar else moeda(res)


def aumentar(price: float, taxa: int, formatar=False):
    """
    -> Calcula o aumento de um determinado preço,
    retornando o resultado com ou sem formatação.

    :param price: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem do aumento.
    :param formatar: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formatação.
    """
    res = price + (taxa / 100 * price)
    return res if formatar is False else moeda(res)


def diminuir(price: float, taxa: int, formatar=False):
    """
    -> Retorna a redução do preço por meio de uma porcentagem.

    :param price: o preço que se quer reajustar.
    :param taxa: qual é a porcentagem da redução.
    :param formatar: quer a saída formatada ou não?
    :return: o valor reajustado, com ou sem formatação.
    """
    res = price - (taxa / 100 * price)
    return res if not formatar else moeda(res)


def moeda(price: float):
    """
    -> Formata a saída.

    :param price: Preço.
    :return: Uma string.
    """
    return f'R${price:.2f}'.replace('.', ',')


def resumo(price: float, aum: int, red: int):
    """
    -> Mostra o resumo usando todas as outras funções.

    :param price: o preço que se quer exibir.
    :param aum: % de aumento.
    :param red: % de redução.
    :return: Sem retorno.
    """
    print(f"{'-' * 30}\n"
          f"{'RESUMO DO VALOR'.center(30)}\n"
          f"{'-' * 30}")
    print(f"Preço analisado: \t{moeda(price)}\n"
          f"Dobro do preço: \t{dobro(price, True)}\n"
          f"Metade do preço: \t{metade(price, True)}\n"
          f"{aum}% de aumento: \t{aumentar(price, aum, True)}\n"
          f"{red}% de redução: \t{diminuir(price, red, True)}\n"
          f"{'-' * 30}")
