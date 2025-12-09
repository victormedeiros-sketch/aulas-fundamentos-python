# Crie um programa que tenha uma função
# que vai receber como parâmetro o ano de
# nascimento de uma pessoa e que crie um
# ficheiro que informe se a pessoa já pode
# tirar a carta de condução, se precisa de
# autorização do encarregado de educação
# ou se não pode.

# +18 anos – pode
# -16 anos – não pode
# -18 e +16 – com autorização



from datetime import datetime
from pathlib import Path



def carta_conducao(ano_nascimento):
    """
    Recebe o ano de nascimento de uma pessoa, calcula a sua idade,
    determina o seu estatuto para tirar a carta de condução e grava
    a informação num ficheiro.

    """
    ano_atual = datetime.today().year
    idade = ano_atual - ano_nascimento


    if idade >= 18:
        autorizacao = f"Com {idade} anos, a pessoa já pode tirar a carta de condução."

    elif idade >= 16:
        autorizacao = f"Com {idade} anos, a pessoa PODE tirar a carta de condução COM AUTORIZAÇÃO do encarregado de educação."

    else:
        autorizacao = f"Com {idade} anos, a pessoa AINDA NÃO PODE tirar a carta de condução."


    ficheiro = Path("autorizacao_conducao.txt")

    with ficheiro.open('w', encoding='utf-8', errors='ignore') as file:
        file.write("--- Relatório Carta de condução ---\n")
        file.write(f"Ano de Nascimento: {ano_nascimento}\n")
        file.write(f"Ano Atual: {ano_atual}\n")
        file.write(f"Idade Calculada: {idade} anos\n")
        file.write(f"=================================================\n")
        file.write(autorizacao + "\n")
        file.write("=================================================\n")

    print(f'\nSucesso! Informação gravada no ficheiro "{ficheiro}"')
    print(autorizacao)




print("--- Verificador para Carta de Condução ---")
while True:
    carta_conducao(int(input("Introduza o ano de nascimento: ")))
    break




