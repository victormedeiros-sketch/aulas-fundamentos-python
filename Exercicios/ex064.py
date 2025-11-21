# Crie um programa que leia o nome e a
# média de um aluno, calculando a sua
# situação, tudo dentro de um dicionário.
# No final mostre todo o conteúdo do dicionário.

# Situação:
# Média >= 9,5 – Aprovado
# Média < 9,5 - Reprovado

aluno = {}

aluno['Nome'] = input(f'Digite o nome do aluno:  ')
aluno['Média'] = float(input(f"Digite a media do {aluno['Nome']}: "))

if aluno['Média'] > 9.5:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'


print(aluno)
