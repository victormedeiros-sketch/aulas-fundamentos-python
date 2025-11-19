#Crie um menu simples de registro e login
#No registro guarda o username e passsword de um utilizador numa tuple
#no login, se o utilizador errar os dados 3 vezes devera aparecer uma mensagem a dizer conta bloqueada e o programa termina


tentativas = 0
while True:
    print('---MENU---')
    print('[1] - Registro')
    print('[2) - Login')

    opcao = int(input('Escolha uma das opções: '))

    if opcao == 1:
        print('---Registo de utiliizador---')
        dados = input('Username: '), input('Senha: ')
        print('Utlizador registado com sucesso!')

    elif opcao == 2:

        while tentativas < 3:
            usernameinput = input('Username. ')
            passwordinput = input('Password: ')
            tentativas += 1

            if dados[0] == usernameinput and dados[1] == passwordinput:
                print('Login efetuado com sucesso! ')
                break

            else:
                print('DADOS INVÁLIDOS')
    if tentativas == 3:
        print('CONTA BLOQUEADA')
        break


