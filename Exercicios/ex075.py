# Crie um programa que tenha uma função
# que receba um número inteiro e mostre a
# tabuada desse número.

def tabuada(num):
    print('__TABUADA__')
    for c in range(0,10):
        print(f'{c+1} x {num} = {(c+1)*num}')




tabuada(2)
