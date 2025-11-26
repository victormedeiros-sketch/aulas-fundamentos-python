# Crie um programa que tenha uma função
# que receba um texto como parâmetro e que
# mostre uma mensagem com tamanho adaptável.


def titulo(txt):
    tam = len(txt) + 4
    print('_'*tam)
    print(f'  {txt}')
    print('_'*tam)


titulo('ESTOU A APRENDER PYTHON')

