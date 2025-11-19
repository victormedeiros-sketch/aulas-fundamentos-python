# Faça um programa que leia o ano de nascimento de 7 pessoas e
# mostre quantas são maiores de idade e
# quantas não são maiores de idade.

from datetime import datetime
qtd_maiores = 0
qtd_menores = 0

ano_atual = datetime.now().year

for c in range(0,7):
    ano_nascimento  = int(input(f'Digite o ano de nascimento da {c+1}ª pessoa: '))

    idade = ano_atual - ano_nascimento

    if idade >= 18:
        qtd_maiores += 1
    else:
        qtd_menores += 1

print(f' há {qtd_maiores} pessoas maiores de idade.')
print(f' há {qtd_menores} pessoas menores de idade.')