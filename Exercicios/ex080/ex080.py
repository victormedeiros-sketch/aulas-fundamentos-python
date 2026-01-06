# Crie um programa com uma função que vai
# receber várias notas de alunos e vai
# retornar um dicionário com o seguinte:
#
# a) Quantidade de notas
# b) A maior nota
# c) A média da turma
# d) A situação (lógico opcional)
# >12 – boa
# <9,5 – fraca
# >9,5 e <12 - razoável

def relacao_notas():
    turma = {}
    qtd_notas = 0
    maior_nota = 0
    soma_nota = 0
    while True:
        nota = float(input('Nota: '))
        qtd_notas += 1
        soma_nota += nota
        media = soma_nota / qtd_notas
        if maior_nota == 0:
            maior_nota = nota
        else:
            if nota > maior_nota:
                maior_nota = nota
        cont = input('Continuar? [s/n] ').lower()
        if 's' in cont:
            continue
        elif 'n' in cont:
            break
        else:
            print('Resposta inválida')
            cont = input('Continuar? [s/n] ').lower()

    turma['Quantidade de notas'] = qtd_notas
    turma['Maior Nota'] = maior_nota
    turma['Media da turma'] = media

    if media >= 12:
        turma['Situação'] = 'Boa'
    elif media <= 9.5:
        turma['Situação'] = 'Fraca'
    else:
        turma['Situação'] = 'Razoavel'
    print(turma)











