# Programa que leia dois valores
# Mostre na tale um menu de escolha(somar,multiplicar,maior,novos numeros,sair do ptograma)

num1 = int(input('Escolha um numero: '))
num2 = int(input('Escolha outro numero: '))
escolha = ''

while escolha != 5:
    print('MENU:')
    print('[1] - Somar')
    print('[2] - Multiplicar')
    print('[3] - Maior')
    print('[4] - Novos números')
    print('[5] - Sair')
    escolha = int(input('Escolha uma das opções de 1 a 4: '))

    if escolha == 1:
        print(f'{num1} + {num2} = {num1 + num2}')

    elif escolha == 2:
        print(f'{num1} x {num2} = {num1 * num2}')

    elif escolha == 3:
        if num1 > num2:
            print(f'{num1} é maior que {num2}')
        elif num1 < num2:
            print(f'{num2} é maior que {num1}')
        else:
            print('Os números são iguais')

    elif escolha == 4:
        num1 = int(input('Escolha um numero: '))
        num2 = int(input('Escolha outro numero: '))

    else:
        if escolha != 5:
            print('Opção inválida')


print('SAIR... ...')







