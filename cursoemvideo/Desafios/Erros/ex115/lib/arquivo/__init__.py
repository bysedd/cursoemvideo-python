def arquivoExiste(nome: str):
    try:
        open(nome, 'xt')
    except FileExistsError:
        return True
    else:
        return False


def criarArquivo(nome: str):
    try:
        a = open(nome, 'wt+')
        a.close()
    except Exception as erro:
        print(f'\033[31mERRO: "{erro.__class__}" na criação do arquivo!\033[m')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


# noinspection PyUnboundLocalVariable
def lerArquivo(nome: str):
    from Desafios.Erros.ex115.lib.interface import titulo
    try:
        a = open(nome, 'rt')
    except Exception as erro:
        print(f'\033[31mERRO: "{erro.__class__}" ao ler o arquivo!')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.strip('\n').split(';')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq: str, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except Exception as erro:
        print(f'\033[31mERRO: "{erro.__class__}" na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except Exception as erro:
            print(f'\033[31mERRO: "{erro.__class__}" na hora de escrever os dados!\033[m')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
