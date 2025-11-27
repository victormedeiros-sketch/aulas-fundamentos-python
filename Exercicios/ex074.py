# Crie um programa que tenha uma função
# que receba o nome de um aluno e uma
# lista das suas notas. Ele deve calcular
# a média do aluno e mostrar no ecrã o
# nome do aluno, a sua média e se ele
# ficou aprovado ou não.

def  aluno_media(*dados):
    media = 0
    qtd = 0
    nome = ''
    for n in dados:
        if nome == '':
            nome += n
        else:
            qtd += 1
            media += n

    print(f'A média das notas é {media / qtd}')



aluno_media('Victor', 10,10,10)



