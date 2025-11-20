# Cria um programa que crie palpites para a euromilhões.
# O programa deve perguntar quantas chaves serão geradas
# e deve sortear aleatoriamente 5 números de 1 a 50 [sem repetir].
# e duas estrelas de 1 a 12 [sem repetir]. Cada sorteio deve ser guardado numa lista composta.

from random import randint

print('---Gerador de palpites Euromilhões---')

n_palpites = int(input('Quantos palpites deseja gerar?\n--->  '))

for c in range(n_palpites):
    palpite = []
    numeros = []
    estrelas = []

    while len(numeros) < 5:
        numero = randint(0,50)
        if numero not in numeros:
            numeros.append(numero)

    while len(estrelas) < 2:
        estrela = randint(1,12)
        if estrela not in estrelas:
            estrelas.append(estrela)

    palpite.append(numeros[:])
    palpite.append(estrelas[:])

    for indice, linha in enumerate(palpite):
        if indice == 0:
            for numero in linha:
                print(f'{numero}|', end='')
        else:
            for estrela in linha:
                print(f'{estrela}|', end='')




