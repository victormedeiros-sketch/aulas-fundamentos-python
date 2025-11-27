# Crie um programa que tenha uma função
# que receba vários parâmetros como
# valores inteiros. O programa deve
# analisar todos os valores e dizer qual
# deles é o maior.


def numeros(*num):
    maior = 0           #maior = max(num)
    for v in num:
        if v == 0:
            maior = v
        else:
            if v > maior:
                maior = v
    print(f'O maior número é {maior}')



numeros(2,5,10)



