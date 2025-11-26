# Crie um programa que tenha uma função
# chamada area() que receba as dimensões
# de um terreno e mostre a área do
# terreno.

def area():
    f = float(input('Qual o comprimento da frente do terreno? '))
    l = float(input('Qual o comprimento da lateral do terreno? '))
    print(f'A área do terreno de {f}m por {l}m é {f*l}m²')

area()


