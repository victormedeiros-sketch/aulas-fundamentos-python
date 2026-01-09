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

def analisar_notas(*notas, situacao=False):
    res = {}
    res['quantidade'] = len(notas)
    res['maior'] = max(notas)
    res['media'] = sum(notas) / len(notas)

    if situacao:
        if res['media'] > 12:
            res['situacao'] = 'boa'
        elif res['media'] < 9.5:
            res['situacao'] = 'fraca'
        else:
            res['situacao'] = 'razoável'

    return res


def guarda(txt: str) -> None:
    from pathlib import Path

    caminho = Path(r'analisa.txt')

    with caminho.open('a', encoding='utf-8', errors='ignore') as file:
        file.write(f'{txt}\n')






resultado = guarda(analisar_notas(12,1,1.2,7.2,9,situacao=True))
print('Notas inseridas com sucesso!')









