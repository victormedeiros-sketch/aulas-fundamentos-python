# Crie um programa que leie um número de 0 a 20 introduzido pelo utilizador
# Depois deverá mostrar por extenso o número introduzido.

numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'treze',
           'catorze','quinze', 'dezesseis', 'dezessete', 'dezoio',
           'dezenove', 'vinte')

numero = int(input('Digite um número de 0 a 20.'))

print(numeros[numero])
