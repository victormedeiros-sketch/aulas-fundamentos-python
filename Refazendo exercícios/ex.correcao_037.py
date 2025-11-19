#ler um numero e dizer se é ou não um número primo

numero = int(input('Digite um número: '))

contador = 0

for c in range(0,numero):
    if numero % (c+1) == 0:
        contador = contador + 1

if contador == 2:
    print(f'O numero {numero} é primo')
else:
    print(f'O numero {numero} não é primo')




