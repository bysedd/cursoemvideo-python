def titulo(txt: str):
    print(f"{'-' * (len(txt) + 4)}\n{txt:^{len(txt) + 4}}\n{f'-' * (len(txt) + 4)}")


def area(largura: float, comprimento: float):
    print(f'A área de um terreno {largura}x{comprimento} é de {largura * comprimento}m².')


titulo('Controle de Terrenos')
area(float(input('LARGURA (m): ')), float(input('COMPRIMENTO (m): ')))
