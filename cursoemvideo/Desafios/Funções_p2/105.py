def notas(*n: float, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar uma situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    print('-=' * 40)
    d = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'média': float(f'{(sum(n) / len(n)):.1f}')
    }
    if sit:
        if d['média'] >= 7:
            d['situação'] = 'BOA'
        elif d['média'] >= 5:
            d['situação'] = 'RAZOÁVEL'
        else:
            d['situação'] = 'RUIM'
    return d


resp = notas(9.4, 10, 7.5, 10, 7.6, 8, 10, 7.9, 10, 6.5, 8, sit=True)
print(resp)
# print(help(notas))
