# Crie um programa que guarde o
# aproveitamento de um jogador de
# futebol. O programa deverá ler o nome,
# quantos jogos jogou e a quantidade de
# golos por jogo e guardar tudo num
# dicionário. No dicionário, deve
# calcular a média de golos por jogo.

jogador = dict()

jogador['Nome'] = input('Digite o nome do Jogador: ')
jogador['Quantidade de jogos'] = int(input('Digite quantos jogos jogou: '))
jogador['Quantidade de golos'] = int(input('Digite quantos golos marcou: '))
jogador['Média de golos'] = jogador['Quantidade de golos'] / jogador['Quantidade de jogos']

for chave, valor in jogador.items():
    print(f'{chave} -> {valor}')