# Escreva um programa que faça o computador pensar em um número inteiro de 0 a 5
# O usuario tenta descobrir qual foi o numero
# O programa deverá escrever na tela se o usuário ganhou ou perdeu

from random import randint
PC = randint(0,5)


print('-----------------JOGO DA ADIVINHA-----------------')
print('Pensei em um número de 0 a 5. Consegue adivinhar?')
jogador = int(input('--->'))

if PC == jogador:
    print('Parabens! Você ganhou!')
    print(f'Eu pensei em {PC} e voçê escolheu {jogador}')

else:
    print(f'PERDEU! Eu pensei em {PC} e voçê esconheu {jogador}')


