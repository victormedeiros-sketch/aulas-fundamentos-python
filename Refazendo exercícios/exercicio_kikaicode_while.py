# Pedir ao utilizador para escrever a palavra passe kikaicode
# Enquanto a palavra não for a certa deve negar o acesso

palavra_passe = 'kikaicode'
palavra_secreta = 'Flor de Liz'

while True:
    password = input('DIGITE A PALAVRA-PASSE PARA DESCOBRIR A PALAVRA SECRETA. ---> ')
    if palavra_passe == password:
        break
    else:
        print('NEGADO')

print(f'A palavra secreta é {palavra_secreta} ')

