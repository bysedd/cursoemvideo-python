try:  # operação
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):  # falhou
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:  # falhou
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:  # falhou
    print('\nO usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:  # deu certo
    print(f'O resultado é {r:.1f}')
finally:  # certo/falha
    print('Volte sempre! Muito obrigado!')
