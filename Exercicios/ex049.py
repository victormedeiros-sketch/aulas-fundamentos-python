# jogo do par ou impar
# interrompre quando o jogador perder
# exibe o total de vitórias consecutivas

import random

vitorias = 0

print('-------JOGO PAR OU IMPAR-------')

while True:
    jogada_num = int(input('Digite um valor de 0 a 5: '))
    if jogada_num > 5 or jogada_num < 0:
        print('Digite um valor de 0 a 5: ')
        continue

    while True:
        jogada_pi = input('[PAR OU IMPAR]:').strip().lower()
        if jogada_pi == 'par' or jogada_pi == 'impar':
            break
        else:
            print('Por favor digite par ou impar')

    CPU = random.randint(0,5)
    res = CPU + jogada_num


    if res % 2 == 0 and jogada_pi == 'par':
        print(f'jogador: {jogada_num}')
        print(f' CPU: {CPU}')
        print('Você ganhou!')


    else:
        print(f'jogador: {jogada_num}')
        print(f' CPU: {CPU}')
        print('Você perdeu!')
        break
    vitorias += 1


print(f'Total de vitórias: {vitorias}')





