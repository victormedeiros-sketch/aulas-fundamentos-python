opcao = ''
caracter =  '*'
espaco = ' '
qt_espacos = 5
espacos_arvore = 9



while True:

    print('---DESENHADOR DE FORMAS---')
    print('[1] ESCADA A ESQUERDA: ')
    print('[2] ESCADA A DIREITA: ')
    print('[3] TRIANGULO: ')
    print('[4] x: ')

    opcao = int(input('Escolha uma das opções do menu: '))

    if opcao == 1:
        for c in range(0,5):
            print(caracter*(c+1))


    elif opcao == 2:
        for c in range(0, 5):
            num_caracteres = c + 1
            num_espacos = 5 - num_caracteres

            print((espaco * num_espacos) + (caracter * num_caracteres))

    elif opcao == 3:
        for c in range(0,9, 2):
            print(espaco * qt_espacos + (caracter+(caracter*c)))
            qt_espacos -= 1

    elif opcao == 4:
        caracter = '*'
        espaco = ' '
        linha = ''
        for c in range(0,5):
            linha_atual = c - 1 - c

            for d in range(0,5):
                if d == c or c == linha_atual:
                    linha += caracter
                else:
                    linha += espaco
            print(linha)





















