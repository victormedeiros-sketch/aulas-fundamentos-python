# Crie um programa que tenha uma função
# que converta a temperatura de Celsius
# para Fahrenheit.

def conversor(temp):
    print(f'{(temp*1.8)+32}ºF')



conversor(int(input('Digite a temperatura em ºC para converter em ºF: ')))