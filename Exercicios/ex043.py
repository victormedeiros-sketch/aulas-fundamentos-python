# Programa que leia tres numeros
# mostrar o menu 1 - somar / 2 - multiplicar / 3 - maior / 4 - novos numeros / 5 - sair do programa
# programa realiza a ação solicitada

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))
num3 = int(input('Digite mais um número: '))

print('Escolha uma das opções:')
print('[1] Somar ')
print('[2] Multiplicar ')
print('[3] Maior ')
print('[4] Novos números ')
print('[5] Sair ')

opcao = ''
while opcao != 5:

    opcao = int(input('Digite o número correspontente a opção desejada: '))

    if opcao == 1:
        print(f'{num1} + {num2} + {num3} = {num1 + num2 + num3}')
    elif opcao == 2:
        print(f'{num1} x {num2} x {num3} = {num1 * num2 * num3}')
    elif opcao == 3:
        if num1 > num2 and num1 > num3:
            print(f'{num1} é o número maior')
        elif num2 > num1 and num2 > num3:
            print(f'{num2} é o número maior')
        elif num3 > num1 and num3 > num2:
            print(f'{num3} é o número maior')
        else:
            print('Os números são iguais')
    elif opcao == 4:
        print('\n--- Digite os NOVOS números ---')
        num1 = int(input('Digite o NOVO primeiro número: '))
        num2 = int(input('Digite o NOVO segundo número: '))
        num3 = int(input('Digite o NOVO terceiro número: '))
        print('Novos números registrados! Escolha a próxima ação no menu.')


print('Sair do programa')