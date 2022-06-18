def voto(nascimento: int):
    from datetime import date
    idade = date.today().year - nascimento
    if 0 <= idade <= 119:
        print(f'Com {idade} anos: ', end='')
        if 18 <= idade <= 65:
            return 'VOTO OBRIGATÓRIO.'
        elif idade >= 16:
            return 'VOTO OPCIONAL.'
        else:
            return 'NÃO VOTA'
    else:
        return f'\033[1:31mIDADE INVÁLIDA\033[m'


print('-' * 30)
print(voto(int(input('Em que ano você nasceu? '))))
