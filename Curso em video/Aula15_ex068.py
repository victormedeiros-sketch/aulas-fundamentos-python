#Program que jogue par ou impar com o computador
#interrompe quando o jogador perder
#mostrando o total de vitorias consecutivas que ele conquistou no fim do jogo

from random import randint

vitorias = 0

while True:
    print('-+-+-+JOGO PAR OU IMPAR-+-+-+')

    print('Escolha um número entre 1 e 10: ')
    num = int(input('---> '))

    print('Digite [1] para Par ou [2] para impar: ')
    escolha = int(input('---> '))

    comp = randint(0, 10)

    if escolha == 1:
        if num % 2 == 0 and comp % 2 == 0:
            print(f'Você escolheu {num} e eu escolhi {comp}\n Parabens, você ganhou!')
            vitorias += 1
        else:
            print(f'Você escolheu {num} e eu escolhi {comp}\n Você perdeu!')
            break

    if escolha == 2:
        if num % 2 == 1 and comp % 2 == 1:
            print(f'Você escolheu {num} e eu escolhi {comp}\n Parabens, você ganhou!')
            vitorias += 1
        else:
            print(f'Você escolheu {num} e eu escolhi {comp}\n Você perdeu!')
            break

print(f'Fim do jogo\n Nessa rodada você perdeu.\n Vitórias consecutivas: {vitorias} ')





