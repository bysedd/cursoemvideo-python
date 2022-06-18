from datetime import datetime

dados = {'nome': input('Nome: ').title()}
ano_nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
dados['idade'] = ano_atual - ano_nascimento
dados['cpts'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados.get('cpts') != 0:
    dados['contratação'] = int(input('Ano de Contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = 35 - (ano_atual - dados['contratação']) + dados['idade']
print('-=' * 30)
for k, v in dados.items():
    print(f'  - {k} tem o valor {v}')
