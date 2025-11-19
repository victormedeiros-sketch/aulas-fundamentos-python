# mostrar numeros pares entre 1 e 100

for c in range(0,100):
    numero = c
    if numero % 2 == 0 and numero != 0:
        print(f'{c} é par')
