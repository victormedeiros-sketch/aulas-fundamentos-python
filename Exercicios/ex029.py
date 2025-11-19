# Crie o seguinte menu: --- Calculadora --- [ 1 ] – Tabuada [ 2 ] – Calculadora [ 3 ] – Números Pares [ 4 ] – Sair
# Mediante a opção solicitada o sistema deve executar a ação do menu.


print('---Calculadora---')
print('[1] - Tabuada')
print('[2] - Calculadora')
print('[3] - Números pares')
print('[4] - Sair')

opcao = int(input('Digite o número referente ao programa que deseja executar: '))


if opcao == 1:
    print('---Tabuada---')

    num = int(input('Escolha um número - '))

    if num:
        print('1 x', num, '=', num * 1)
        print('2 x', num, '=', num * 2)
        print('3 x', num, '=', num * 3)
        print('4 x', num, '=', num * 4)
        print('5 x', num, '=', num * 5)
        print('6 x', num, '=', num * 6)
        print('7 x', num, '=', num * 7)
        print('8 x', num, '=', num * 8)
        print('9 x', num, '=', num * 9)
        print('10 x', num, '=', num * 10)

elif opcao == 2:
    print('---Calculadora---')

    calculo = input('Digite o cálculo: ')
    calculo = calculo.strip().replace(' ','')

    if '+' in calculo:
        posicao = calculo.find('+')
        num1 = int(calculo[:posicao])
        num2 = int(calculo[posicao + 1:])
        print(f'{num1} + {num2} = {num1 + num2}')

    elif '-' in calculo:
        posicao = calculo.find('-')
        num1 = int(calculo[:posicao])
        num2 = int(calculo[posicao + 1:])
        print(f'{num1} - {num2} = {num1 - num2}')

    elif '*' in calculo or 'x' in calculo:
        if 'x' in calculo:
            posicao = calculo.find('x')
        else:
            posicao = calculo.find('*')

        num1 = int(calculo[:posicao])
        num2 = int(calculo[posicao + 1:])
        print(f'{num1} x {num2} = {num1 * num2}')

    elif '/' in calculo:
        posicao = calculo.find('/')
        num1 = int(calculo[:posicao])
        num2 = int(calculo[posicao +1:])
        if num2 == 0:
            print('Não é possível dividir por ZERO ')
        else:
            print(f'{num1} / {num2} = {num1 / num2}')

elif opcao == 3:
    print('---Números pares---')
    numero = int(input('Digite um número: '))

    if numero % 2 == 0:
        print(f'{numero} é PAR')
    else:
        print(f'{numero} é IMPAR')

elif opcao == 4:
    print('A sair...')

else:
    print('Opção inválida...')



























