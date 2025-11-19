# Eu quero criar um programa que peça o género de uma pessoa
# Apenas aceita como resposta "M" ou "F"
# Se o utilizador digitar outra resposta ele vai ter de pedir novamente
genero = ' '
while genero != 'M' and genero != 'F':
    genero = input('Digite o seu género: ').strip().upper()
