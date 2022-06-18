def fatorial(n: int):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    return f


def mult(n: int, vezes: int):
    return n * vezes
