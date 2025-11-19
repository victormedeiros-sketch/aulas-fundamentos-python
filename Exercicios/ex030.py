# Crie o jogo pedra, papel, tesoura.

from random import randint

print('---Pedra, papel ou tesoura?---')

print('1 - Pedra')
print('2 - Papel')
print('3 - Tesoura')

jogador = int(input('Digite o número referente a opção escolhida: '))

cpu = randint(1,3)

if jogador == 1:
    if cpu == 1:
        print('Empate')
        print(f'CPU: {cpu}')
        print(f'Jogador:{jogador}')
    elif cpu == 2:
        print('CPU ganhou')
        print(f'CPU: {cpu}')
        print(f'Jogador:{jogador}')
    elif cpu == 3:
        print('Jogador ganhou')
        print(f'CPU: {cpu}')
        print(f'Jogador:{jogador}')

if jogador == 2:
    if cpu == 1:
        print('Jogador ganhou')
        print(f'CPU: {cpu}')
        print(f'Jogador:{jogador}')
    elif cpu == 2:
        print('EMPATE!!!')
        print(f'CPU: {cpu}')
        print(f'Jogador:{jogador}')
    elif cpu == 3:
        print('CPU ganhou')
        print(f'CPU: {cpu}')
        print(f'Jogador:{jogador}')

elif jogador == 3:
    if cpu == 1:
        print('CPU ganhou')
        print(f'CPU: {cpu}')
        print(f'Jogador:{jogador}')
    elif cpu == 2:
        print('Jogador ganhou!!')
        print(f'CPU: {cpu}')
        print(f'Jogador:{jogador}')
    elif cpu == 3:
        print('EMPATE!!!')
        print(f'CPU: {cpu}')
        print(f'Jogador:{jogador}')

else:
    print('...Jogada invalida...')








