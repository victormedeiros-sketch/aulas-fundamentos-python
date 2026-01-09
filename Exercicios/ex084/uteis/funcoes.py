import operator
import math
def titulo(txt: str) -> None:
    tam = len(txt) + 4
    print('_' * tam)
    print(f'{txt:^{tam}}')
    print('_' * tam)



def calculadora():
    while True:
        titulo('CALCULADORA')
        print('[1] - Soma')
        print('[2] - Subtração')
        print('[3] - Multiplicação')
        print('[4] - Divisão')
        print('[5] - Sair')
        escolha = input('---> ')

        match escolha:
            case '1':
                titulo('SOMA')
                try:
                    n1 = float(input('Digite o primeiro numero: '))
                    n2 = float(input('digite o segundo numero: '))
                    soma = n1 + n2
                    print(f'{n1} + {n2} = {soma}')
                except ValueError:
                    print('Digito inválido')


            case '2':
                titulo('SUBTRAÇÃO')
                try:
                    n1 = float(input('Digite o primeiro numero: '))
                    n2 = float(input('digite o segundo numero: '))
                    sub = n1 - n2
                    print(f'{n1} - {n2} = {sub}')
                except ValueError:
                    print('Digito inválido')

            case '3':
                titulo('MULTIPLICAÇÃO')
                try:
                    n1 = float(input('Digite o primeiro numero: '))
                    n2 = float(input('digite o segundo numero: '))
                    mult = operator.mul(n1,n2)
                    print(f'{n1} x {n2} = {mult}')
                except ValueError:
                    print('Digito inválido')

            case '4':
                titulo('DIVISÃO')
                try:
                    n1 = float(input('Digite o primeiro numero: '))
                    n2 = float(input('digite o segundo numero: '))
                    divi = operator.truediv(n1, n2)
                    print(f'{n1} x {n2} = {divi}')
                except ZeroDivisionError:
                    print('Impossivel dividir por zero')
                except ValueError:
                    print('Digito inválido')

            case '5':
                break

            case _:
                print('opção iniválida')

        input('Enter para continuar...')



def tabuada():
    titulo('TABUADA')
    try:
        num = int(input('Digite o numero que deseja visualizar a tabuada: '))
        for c in range(0,10):
            print(f'{num} x {c+1} = {operator.mul(c+1,num)}')
    except ValueError:
        print('Digito inválido')



def par_ou_impar():
    try:
        titulo('PAR OU IMPAR')
        numero = int(input('Digite um número para saber se é par ou impar: '))
        if numero % 2 == 0:
            print(f'{numero} é par')
        else:
            print(f'{numero} é impar')
    except ValueError:
        print('Digito inválido')



def numeros_primos():
    titulo('ANÁLISE DE NÚMEROS PRIMOS')
    try:
        nump = int(input('Digite um número inteiro para verificar: '))

        if nump <= 1:
            print(f'O número {nump} não é primo.')
        else:
            e_primo = True
            for c in range(2, int(nump ** 0.5) + 1):
                if nump % c == 0:
                    e_primo = False
                    break

            if e_primo:
                print(f'O número {nump} é PRIMO!')
            else:
                print(f'O número {nump} NÃO é primo.')

    except ValueError:
        print('Erro: Entrada inválida! Digite apenas números inteiros.')


def factorial():
    titulo('CÁLCULO DE FACTORIAL')
    try:
        numfat = int(input('Digite um número: '))

        if numfat < 0:
            print("Erro: Não existe factorial de números negativos!")
        else:
            resultado = math.factorial(numfat)
            print(f'O factorial de {numfat} é: {resultado}')

    except ValueError:
        print('Erro: Entrada inválida! Digite apenas números inteiros.')











