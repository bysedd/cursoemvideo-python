from datetime import date

ano = int(input('Ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano
ano_restante = idade - ano
tempo_alistamento1 = 18 - idade
tempo_alistamento2 = idade - 18
ano_alistamento = 18 + ano

if idade < 18:
    print('Quem nasceu em \033[1;30m{}\033[m tem \033[1;30m{}\033[m anos em \033[1;30m{}\033[m.'
          .format(ano, idade, ano_atual))
    print('Ainda faltam \033[1;30m{}\033[m anos para o alistamento'
          .format(tempo_alistamento1))
    print('Seu alistamento será em \033[1;30m{}\033[m.'
          .format(ano_alistamento))
elif idade > 18:
    print('Quem nasceu em \033[1;30m{}\033[m tem \033[1;30m{}\033[m anos em \033[1;30m{}\033[m.'
          .format(ano, idade, ano_atual))
    print('Você já deveria ter se alistado há \033[1;30m{}\033[m anos.'
          .format(tempo_alistamento2))
    print('Seu alistamento foi em \033[1;30m{}\033[m.'
          .format(ano_alistamento))
else:
    print('Quem nasceu em \033[1;30m{}\033[m tem \033[1;30m{}\033[m anos em \033[1;30m{}\033[m.'
          .format(ano, idade, ano_atual))
    print('Você tem que se alistar \033[1;31mIMEDIATAMENTE!\033[m')
