# Crie um programa que tenha uma função
# que receba 3 parâmetros: inicio, fim e
# passo. O programa deve realizar 3
# contagens através da função.

# a) De 1 até 20, de 2 em 2
# b) De 10 até 0, de 1 em 1
# c) Contagem personalizada

from time import sleep

def contagem():
    print('CONTAGEM 1-20 PASSO-2')
    for c in range(1,20,2):
        print(c)
        sleep(0.3)
    print('CONTAGEM 10-0 PASSO-1')
    for c in range(10,0,-1):
        print(c)
        sleep(0.3)
    print('CONTAGEM PERSONALIZADA')
    inicio = int(input('INICIO: '))
    fim = int(input('FIM: '))
    passo = int(input('PASSO: '))

    for c in range(inicio, fim, passo):
        print(c)
        sleep(0.3)

contagem()