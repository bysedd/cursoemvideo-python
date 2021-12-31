largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura

print('Sua parede tem a dimensão de \033[1;32m{}\033[m x \033[1;32m{}\033[m'
      ' e sua área é de \033[1;30m{:.2f}m²\033[m.'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de \033[1;34m{:.2f}l\033[m de tinta.'.format(area / 2))
