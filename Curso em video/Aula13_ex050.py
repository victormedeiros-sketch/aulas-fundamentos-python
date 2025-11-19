soma_pares = 0
for c in range(0,5):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        soma_pares += numero

print(f'A soma dos números pares é {soma_pares} ')
