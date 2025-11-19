print('---Registro de utilizador---')

email_registro = input('EMAIL: ')
senha_registro = input('(mínimo de cinco digitos) SENHA: ').strip()
registro_sucesso = False

if len(senha_registro) >= 5:
    senha_confirma = input('CONFIRMAR SENHA: ').strip()

    if senha_registro == senha_confirma and '@' in email_registro and email_registro.count('@') == 1:
        print('Usuário registrado com sucesso!!!')
        registro_sucesso = True

    else:
        print('O e-mail não é válido ou as senhas não coincidem.')

else:
    print('ERRO: A senha deve conter no mínimo cinco caracteres.')

from time import sleep

if registro_sucesso:
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)
    print('.')
    sleep(0.5)



    print('\n---Menu principal---')
    print('[1] - login ')
    print('[2] - Sair ')

    login = input('Selecione uma opção para seguir: ')
    if login == '1':
        email_login = input('EMAIL: ').strip()
        senha_login = input('SENHA: ').strip()

        if email_login == email_registro and senha_login == senha_registro:
            print('---Bem vindo ao projeto 002---')
        else:
            print('---e-mail ou senha incorretos. ')

    elif login == '2':
        print('***end***')

    else:
        print('Erro')

else:
    print('\nO registro falhou. Encerrando o programa.')


























