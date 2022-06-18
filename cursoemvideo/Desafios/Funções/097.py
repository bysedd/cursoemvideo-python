def escreva(txt: str):
    tam = len(txt) + 4
    print(f"{'~' * tam}\n"
          f"{txt:^{tam}}\n"
          f"{f'~' * tam}")


escreva('Gustavo Guanabara')
escreva('Curso de Python no YouTube')
escreva('CeV')
