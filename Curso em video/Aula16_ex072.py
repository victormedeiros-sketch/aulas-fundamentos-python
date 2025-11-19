#Um programa que tenha uma tuple totalmente preenchida com  uma contagem de 0 a 20 por extenso
#O programa deve ler o numero de 0 a 20 e mostra-lo por extenso

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


for num in range(0,20):
    num = int(input('Digite um número de 0 a 20: '))
    print(numeros[num])