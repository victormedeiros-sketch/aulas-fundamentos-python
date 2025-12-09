# Crie um programa que leia o nome e a
# média de um aluno, calculando a sua
# situação, tudo dentro de um dicionário.
# No final mostre todo o conteúdo do dicionário.
# Situação:
# Média >= 9,5 – Aprovado
# Média < 9,5 - Reprovado


aluno = {'Nome': input('Digite o seu nome: '),
         'Média': float(input('Digite a sua média: '))
         }

if aluno['Média'] >= 9.5:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

# aluno['Situação'] = 'Aprovado' if if aluno['Média'] >= 9.5 else 'Reprovado'

for chave, valor in aluno.items():
    print(f'{chave} -> {valor}')
