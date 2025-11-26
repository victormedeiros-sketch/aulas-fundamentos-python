# Crie um programa que leia o nome, sexo e
# idade de várias pessoas, guardando cada
# dado num dicionário e todos os
# dicionários numa lista. No final mostre:
#
# a) Quantas pessoas foram registadas;
# b) Qual a média de idades do grupo;
# c) Quantas mulheres foram registadas;
# d) Quantos homens com idade acima da média foram registados.

pessoas = []
dados = dict()
qtd_pessoas = 0
soma_idades = 0
qtd_mulheres = 0

while True:
    dados['nome'] = input('Nome: ').strip()
    while True:
        dados['sexo'] = input('Sexo: ').strip().lower()
        if dados['sexo'] != 'm' and dados['sexo'] != 'f':
            print('Por favor introduza o sexo válido.')
        else:
            break

    if dados['sexo'] == 'f':

    dados['idade'] = input('Idade: ')
    soma_idades += dados['idade']
    pessoas.append(dados.coppy())
    qtd_pessoas += 1
    dados.clear()

    opcao = input('Digite sim para terminar').strip().lower()
    if opcao == 'sim':
        break

media_idades = round(soma_idades / qtd_pessoas, 2)
qtd_homesn_acima_media = 0

for pessoa in pessoas:
    if pessoa['sexo'] == 'm':
        if pessoa['idade'] > media_idades:
            qtd_homens_acima_media += 1

print('#'*30)
print('Informações:')
print(f'Foram registrados {qtd_pessoas} pessoas')
print(f'Amedia de idade é {media_idades} anos.')
print(f'Foram registradas {qtd_mulheres} mulheres')
print(f'Foram registrados {qtd_homens_acima_media} homens com idade acima da media')