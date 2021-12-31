lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
# Tuplas são IMUTÁVEIS
# lanche[1] = 'Refrigerante'
for comida in lanche:
    print(f'Eu vou comer {comida}')
print()
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na posisão {cont}')
print()
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posisão {pos}')
print()
print('Comi pra caramba!')
