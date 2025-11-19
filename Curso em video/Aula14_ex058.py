#jogo da adivinha
print('----------------------')
print('***JOGO DA ADIVINHA***')
print('----------------------')
from random import randint
computador = randint(0,10)
print('Pensei em um número de 0 a 10.')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Adivinhe o número: '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente!')
        elif jogador > computador:
            print('Menos... Tente novamente')

print(f'Acertou com {palpites} tentativas!')






