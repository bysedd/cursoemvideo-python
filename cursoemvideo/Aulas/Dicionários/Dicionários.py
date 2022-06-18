"""
locadora = [
    {
        'titulo': 'Star Wars',
        'ano': 1977,
        'diretor': 'George Lucas'
    },
    {
        'titulo': 'Avengers',
        'ano': 2012,
        'diretor': 'Joss Whedon'
    },
    {
        'titulo': 'Matrix',
        'ano': 1999,
        'diretor': 'Wachowski'
    }
]
for filme in locadora:
    print(f"Nome: {filme.get('titulo')}")
    print(f"Ano: {filme.get('ano')}")
    print(f"Diretor: {filme.get('diretor')}")
print()

brasil = [
    {
        'uf': 'Rio de Janeiro',
        'sigla': 'RJ'
    },
    {
        'uf': 'São Paulo',
        'sigla': 'SP'
    }
]

for estado in brasil:
    print(f"Unidade Federativa: {estado.get('uf')}")
    print(f"Sigla: {estado.get('sigla')}")
"""

estado = dict()
brasil = list()
for _ in range(3):
    estado['uf'] = input('Unidade Federativa: ').title()
    estado['sigla'] = input('Sigla: ').upper()
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()
