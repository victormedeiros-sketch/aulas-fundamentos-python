# Crie um programa que tenha uma função
# que receba vários parâmetros como
# valores inteiros. O programa deve
# analisar todos os valores e dizer qual
# deles é o maior.

def pede_numero():
    n_maior = 0
    while True:
        n = int(input('Digite um número: '))
        if n_maior == 0:
            n_maior = n
        else:
            if n > n_maior:
                n_maior = n

        qc = input('Quer continuar? [S/N] ').upper()
        if 'S' in qc:
            continue
        elif 'N' in qc:
            break
        else:
            print('Comando inválido, tente novamente.')
            qc = input('Quer continuar? [S/N] ').upper()
    print(f'O maior número digitado foi {n_maior}')


pede_numero()


