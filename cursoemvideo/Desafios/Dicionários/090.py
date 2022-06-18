aluno = {'nome': input('Nome: ')}
aluno['média'] = float(input(f"Média de {aluno['nome']}: "))
if aluno['média'] >= 7.0:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5.0:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'
print(f"{'-=' * 30}")
for k, v in aluno.items():
    print(f"  - {k} = {v}")
