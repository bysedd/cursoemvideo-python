from time import sleep

c = ('\033[m',  # sem cores
     '\033[0;30;41m',  # vermelho
     '\033[0;30;42m',  # verde
     '\033[0;30;43m',  # amarelo
     '\033[0;30;44m',  # roxo
     '\033[0;30;45m',  # rosa
     '\033[0;30;46m',  # azul
     '\033[7m')  # branco


def escreva(txt: str, color=0):
    """
    -> Escreve um texto formatado.
    :param txt: conteúdo do texto.
    :param color: cores aplicadas ao texto.
    :return: sem retorno.
    """
    tam = len(txt) + 4
    print(f"{c[color]}{'~' * tam}\n"
          f"  {txt}  \n"
          f"{f'~' * tam}\n{c[0]}", end='')


def pyhelp():
    while True:
        escreva('SISTEMA DE AJUDA PyHELP', 2)
        h = input('Função ou Biblioteca > ').lower()
        if h == 'fim':
            escreva('ATÉ LOGO', 1)
            sleep(1)
            break
        else:
            escreva(f"Acessando o manual do comando '{h}'", 6)
            sleep(1)
            print(c[7], end='')
            help(h)
            print(c[0], end='')
        sleep(1)


pyhelp()
