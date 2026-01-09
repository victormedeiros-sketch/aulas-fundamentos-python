# Desenvolva um programa que simule uma calculadora interativa
# com diferentes funcionalidades. O programa deve exibir um
# menu com várias opções e permitir que o utilizador escolha
# uma das opções. O programa deve executar a funcionalidade
# escolhida e quando terminar deve voltar a apresentar o menu.
# Use o tratamento de exceções para lidar com entradas
# inválidas (como strings ou caracteres) e erros matemáticos
# (como divisão por zero). Todas as funções devem estar num
# módulo bem estruturado e documentado.
# Função- Calculadora [SOMA, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO]
# Função- Tabuada
# Função- Par ou Ímpar
# Função- Números primos
# Função- Factorial

from uteis import funcoes

while True:
    funcoes.titulo('MENU DE OPERAÇÕES')
    print('[1] - calculadora')
    print('[2] - Tabuada')
    print('[3] - Par ou impar')
    print('[4] - Números primos')
    print('[5] - Factorial')
    print('[6] - Sair')
    opcao = input('----> ')

    match opcao:
        case '1':
            funcoes.calculadora()
        case '2':
            funcoes.tabuada()
        case '3':
            funcoes.par_ou_impar()
        case '4':
            funcoes.numeros_primos()
        case '5':
            funcoes.factorial()
        case '6':
            print('A sair...')
            break
        case _:
            print('Digite uma opção válida')
    input('Enter para continuar...')
