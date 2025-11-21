# Crie um programa que sorteie a ordem de
# jogada num jogo ao “atirar um dado ao
# ar”. Cada jogador terá um número
# aleatório associado dentro de um
# dicionário. No final ordene o ranking
# para ver a ordem de jogada.

from random import randint
print('-=-=JOGO DE DADOS=-=-')
qtd_jogadores = int(input('Digite quantos jogadores vão jogar: '))
jogadores = {}

for c in range(qtd_jogadores):
    nome = input(f'Digite o nome do {c+1}º jogador')
    jogada = randint(1, 6)
    jogadores[nome] = jogada

auxiliar = jogadores.copy()
ranking = list()

while auxiliar:
    maior_jogador = ''
    maior_valor = 0

    for jogador, jogada in auxiliar.items():
        if jogada > maior_valor:
            maior_jogador = jogador
            maior_valor = jogada
    ranking.append((maior_jogador, maior_valor))
    del auxiliar[maior_jogador]

for tuple in ranking:
    for elemento in tuple:
        print(f'{elemento}', end=' ')

    print()