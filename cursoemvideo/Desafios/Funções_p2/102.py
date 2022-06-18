def fatorial(n: int, show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f, p = 1, ''
    for c in range(n, 0, -1):
        if show:
            p += f'{c} x '
        f *= c
    print('-' * len(str(f)))
    if show:
        return f'{p[:len(p) - 3]} = {f}'
    else:
        return f


print(fatorial(13))
# print(help(fatorial))
