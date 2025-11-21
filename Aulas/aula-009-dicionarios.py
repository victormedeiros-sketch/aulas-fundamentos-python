turma = []
qtd_alunos = 5
aluno = dict()

for c in range(qtd_alunos):

    aluno['Nome'] = input(f'Digite o nome do {c+1}ª aluno:  ')
    aluno['Média'] = float(input(f'Digite a media do {aluno['Nome']}: '))

    if aluno['Média'] > 9.5:
        aluno['Situação'] = 'Aprovado'
    else:
        aluno['Situação'] = 'Reprovado'

    turma.append(aluno.copy())

print(turma)