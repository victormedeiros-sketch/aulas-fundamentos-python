# Crie um programa que tenha uma função
# que receba 3 parâmetros: inicio, fim e
# passo. O programa deve realizar 3
# contagens através da função.

# a) De 1 até 20, de 2 em 2
# b) De 10 até 0, de 1 em 1
# c) Contagem personalizada

from time import sleep

def contador(i,f,p):
    if p < 1:
        p = 1
        print('Passo vai iniciar com  o valor padrão')

    if i > f:
        p = -p
        f = f - 1
    for c in range(i,f,p):
        print(c)


print('Contagem de 1 a 20 com passo 2:')
contador(1,20,2)
print('Contagem regressiva de 10 a 0:')
contador(10,0,1)


print('Contagem personalizada')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contador(inicio,fim,passo)