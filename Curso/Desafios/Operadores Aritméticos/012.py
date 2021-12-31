preço = float(input('Qual o preço do produto? \033[1;32mR$\033[m '))

porcentagem = (preço / 100) * 5
novo_preço = preço - porcentagem

print('O produto que custava \033[1;32mR${}\033[m,'
      ' na promoção com desconto de 5% vai custar \033[1;7;32mR${:.2f}\033[m.'
      .format(preço, novo_preço))
