# Criar jogo da adivinha 2.0
# O computador deve pensar num número de 0 a 10 e o utilizador ta adivinhar até acertar
# No final mostrar quantas tentativas
print('---JOGO DA ADIVINHA V2.0---')

import random
escolha_computador = random.randint(0,10)               # usar from random import randint na próxima

contador = 0
numero = 1

while numero != escolha_computador:
    numero = int(input('Adivinhe o numero que estou a pensar de 0 a 10: '))
    contador += 1

    if numero != escolha_computador:
        if numero > escolha_computador:
            print('Menos')
        elif numero < escolha_computador:
            print('Mais')


print(f'Parabens voce acertou, eu pensei no {escolha_computador} ')
print('contador:', contador)
