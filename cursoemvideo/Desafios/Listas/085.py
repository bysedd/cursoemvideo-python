valores = {'par': [], 'impar': []}
for i in range(7):
    v = int(input(f'Digite o {i + 1}º valor: '))
    if v % 2 == 0:
        valores.get('par').append(v)
    else:
        valores.get('impar').append(v)
print('-=' * 30)
if len(valores.get('impar')) == 0:
    print('Nenhum valor ímpar digitado.')
    print(f"Os valores pares digitados foram: {sorted(valores.get('par'))}")
elif len(valores.get('par')) == 0:
    print('Nenhum valor par digitado.')
    print(f"Os valores ímpares digitados foram: {sorted(valores.get('impar'))}")
else:
    print(f"Os valores pares digitados foram: {sorted(valores.get('par'))}\n"
          f"Os valores ímpares digitados foram: {sorted(valores.get('impar'))}")
